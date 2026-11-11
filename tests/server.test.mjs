import test from 'node:test';
import { createHash } from 'node:crypto';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createWorker } from '../src/server/index.mjs';
import { renderPages } from '../src/render.mjs';
import { collectAttribution } from '../src/server/attribution.mjs';

const site = JSON.parse(await readFile(new URL('../config/site.json', import.meta.url)));
const actualRelease = JSON.parse(await readFile(new URL('../config/release.json', import.meta.url)));
const release = { ...actualRelease, sizeBytes: 4 };
const pages = renderPages(site, release, {
  styles: '/assets/site.css',
  script: '/assets/app.js',
  smsStyles: '/assets/sms.css',
  smsScript: '/assets/sms.js'
});
const asset = { base64: 'aWNvbg==', size: 4, type: 'image/webp', etag: '"test-etag"', immutable: true };
const makeWorker = (fetchImpl, overrides = {}) => createWorker({
  site, release, pages, assets: { '/assets/test.abcd.webp': asset }, fetchImpl, ...overrides
});
const request = (path, options) => new Request(site.origin + path, options);
const sourceResponse = (body = 'APK!', headers = {}, status = 200) => new Response(body, {
  status, headers: { 'Content-Type': 'application/vnd.android.package-archive', 'Content-Length': '4', ...headers }
});

test('download streams the fixed release with attachment headers, without a redirect', async () => {
  let called;
  const worker = makeWorker(async (url, options) => { called = { url, options }; return sourceResponse(); });
  const result = await worker.fetch(request('/download?url=https://other.example/app.apk&utm_source=whatsapp', {
    headers: { Cookie: 'private=value', Authorization: 'Bearer visitor-value' }
  }));
  assert.equal(result.status, 200);
  assert.equal(await result.text(), 'APK!');
  assert.equal(called.url, release.url);
  assert.equal(called.options.redirect, 'error');
  assert.equal(called.options.headers.get('Cookie'), null);
  assert.equal(called.options.headers.get('Authorization'), null);
  assert.equal(result.headers.get('Content-Type'), 'application/vnd.android.package-archive');
  assert.equal(result.headers.get('Content-Disposition').startsWith(`attachment; filename="${release.filename}"`), true);
  assert.equal(result.headers.get('Content-Length'), '4');
  assert.equal(result.headers.get('Location'), null);
  assert.equal(result.headers.get('X-Download-SHA256'), release.sha256);
});

test('HEAD obtains file metadata without transferring an APK body', async () => {
  let method;
  const worker = makeWorker(async (_, options) => { method = options.method; return sourceResponse(null); });
  const result = await worker.fetch(request('/download', { method: 'HEAD' }));
  assert.equal(method, 'HEAD');
  assert.equal(result.status, 200);
  assert.equal(result.headers.get('Content-Length'), '4');
  assert.equal(await result.text(), '');
});

test('a resumable byte range preserves upstream offsets and validator', async () => {
  let sent;
  const worker = makeWorker(async (_, options) => {
    sent = options.headers;
    return sourceResponse('PK', { 'Content-Length': '2', 'Content-Range': 'bytes 1-2/4', ETag: '"apk-version"' }, 206);
  });
  const result = await worker.fetch(request('/download', { headers: { Range: 'bytes=1-2', 'If-Range': '"apk-version"' } }));
  assert.equal(sent.get('Range'), 'bytes=1-2');
  assert.equal(sent.get('If-Range'), '"apk-version"');
  assert.equal(result.status, 206);
  assert.equal(result.headers.get('Content-Range'), 'bytes 1-2/4');
  assert.equal(await result.text(), 'PK');
});

test('invalid multi-range input is rejected before contacting the source', async () => {
  let contacted = false;
  const worker = makeWorker(async () => { contacted = true; return sourceResponse(); });
  const result = await worker.fetch(request('/download', { headers: { Range: 'bytes=0-1,2-3' } }));
  assert.equal(result.status, 416);
  assert.equal(result.headers.get('Content-Range'), 'bytes */4');
  assert.equal(contacted, false);
});

test('unavailable, replaced or unexpected upstream files fail closed with a usable page', async t => {
  const cases = [
    ['network failure', async () => { throw new Error('private upstream details'); }],
    ['redirect', async () => new Response(null, { status: 302, headers: { Location: 'https://other.example/' } })],
    ['HTML response', async () => sourceResponse('<html>', { 'Content-Type': 'text/html' })],
    ['changed full size', async () => sourceResponse('changed', { 'Content-Length': '7' })],
    ['wrong range total', async () => sourceResponse('AP', { 'Content-Length': '2', 'Content-Range': 'bytes 0-1/10' }, 206)],
    ['inconsistent range length', async () => sourceResponse('AP', { 'Content-Length': '3', 'Content-Range': 'bytes 0-1/4' }, 206)]
  ];
  for (const [name, fetchImpl] of cases) await t.test(name, async () => {
    const result = await makeWorker(fetchImpl).fetch(request('/download'));
    const text = await result.text();
    assert.equal(result.status, 503);
    assert.match(text, /Download temporarily unavailable/);
    assert.equal(text.includes(release.url), false);
    assert.equal(text.includes('private upstream details'), false);
    assert.equal(result.headers.get('Retry-After'), '60');
    assert.equal(result.headers.get('X-Robots-Tag'), 'noindex');
  });
});

test('upstream unsatisfiable ranges become a bounded 416 response', async () => {
  const result = await makeWorker(async () => new Response(null, { status: 416 })).fetch(request('/download'));
  assert.equal(result.status, 416);
  assert.equal(result.headers.get('Content-Range'), 'bytes */4');
});

test('campaign attribution reaches both download links without needing JavaScript', async () => {
  const result = await makeWorker().fetch(request('/?utm_source=whatsapp&utm_campaign=launch-a&phone=919876543210&url=https://other.example'));
  const html = await result.text();
  const apkLink = `${actualRelease.url}?utm_source=whatsapp&amp;utm_campaign=launch-a`;
  assert.equal((html.match(new RegExp(`href="${apkLink.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}"`, 'g')) || []).length, 2);
  assert.match(html, new RegExp(`<link rel="canonical" href="${site.origin}/">`));
  assert.equal(html.includes('919876543210'), false);
  assert.equal(result.headers.get('Cache-Control'), 'private, no-store');
  assert.equal(result.headers.has('Set-Cookie'), false);
});

test('attribution accepts campaign labels and excludes obvious personal or injected data', () => {
  assert.deepEqual(collectAttribution(new URLSearchParams({
    utm_source: 'sms', utm_medium: 'broadcast', utm_campaign: 'summer',
    utm_content: 'user@example.com', utm_term: '919876543210', ref: 'https://bad.example',
    source: '\u0000value', campaign_id: 'x'.repeat(101), email: 'a@example.com'
  }), site.attribution), { utm_source: 'sms', utm_medium: 'broadcast', utm_campaign: 'summer' });
});

test('only generated public assets are reachable; source and configuration return 404', async () => {
  const worker = makeWorker();
  for (const path of ['/config/release.json', '/src/server/index.mjs', '/.git/config', '/.env', '/package.json', '/assets/app.js.map', '/__qa/mobile']) {
    const result = await worker.fetch(request(path));
    assert.equal(result.status, 404, path);
    assert.equal(result.headers.get('X-Robots-Tag'), 'noindex');
    assert.equal((await result.text()).includes(release.url), false);
  }
  const result = await worker.fetch(request('/assets/test.abcd.webp'));
  assert.equal(result.status, 200);
  assert.equal(await result.text(), 'icon');
  assert.match(result.headers.get('Cache-Control'), /immutable/);
  const cached = await worker.fetch(request('/assets/test.abcd.webp', { headers: { 'If-None-Match': '"test-etag"' } }));
  assert.equal(cached.status, 304);
  assert.equal(await cached.text(), '');
});

test('SEO routes agree on a clean canonical and contain factual application data', async () => {
  const worker = makeWorker();
  const html = await (await worker.fetch(request('/'))).text();
  assert.equal((html.match(/<h1\b/g) || []).length, 1);
  assert.equal((html.match(/data-gallery=/g) || []).length, 7);
  assert.match(html, /Fast withdrawals/);
  assert.match(html, /JAIHO777 Games/);
  assert.match(html, /18\.6K reviews/);
  assert.match(html, /Priya Patel/);
  assert.match(html, /people found this review helpful/);
  assert.match(html, /Google Play/);
  assert.match(html, /realcashgame\.app/);
  assert.match(html, /favourite money game/);
  assert.equal(html.includes('Works on Jio'), false);
  assert.equal(html.includes('button-size'), false);
  assert.equal(html.includes('promo-banner'), false);
  const schemas = JSON.parse(html.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1]);
  assert.equal(schemas[0].softwareVersion, actualRelease.version);
  assert.equal(schemas[0].downloadUrl, actualRelease.url);
  assert.equal('aggregateRating' in schemas[0], false);
  assert.equal('publisher' in schemas[0], Boolean(site.publisherVerified && site.publisher));
  assert.equal(html.includes('DEMO'), false);
  assert.equal(html.includes('DESIGN DEMO'), false);
  assert.equal(html.includes('Fictional'), false);
  assert.match(html, /Aarav Sharma/);
  assert.match(html, /5M\+/);
  assert.match(html, /Verified App/);
  assert.match(html, /name="robots" content="index,follow/);
  assert.match(await (await worker.fetch(request('/robots.txt'))).text(), /Disallow: \//);
  const sitemap = await (await worker.fetch(request('/sitemap.xml'))).text();
  assert.equal((sitemap.match(/<loc>/g) || []).length, 3);
  assert.equal(sitemap.includes(site.origin + '/sms/'), true);
  assert.equal(sitemap.includes(site.origin + '/privacy/'), true);
  const privacy = await worker.fetch(request('/privacy/'));
  assert.equal(privacy.status, 200);
  assert.match(await privacy.text(), /Website privacy notice/);
  const sms = await worker.fetch(request('/sms/?utm_source=sms&utm_campaign=blast-a'));
  assert.equal(sms.status, 200);
  const smsHtml = await sms.text();
  assert.match(smsHtml, /Withdraw to your bank in minutes/);
  assert.match(smsHtml, /Pay with UPI/);
  assert.equal(smsHtml.includes(`href="${actualRelease.url}?utm_source=sms&amp;utm_campaign=blast-a"`), true);
  assert.equal((await worker.fetch(request('/sms'))).status, 301);
});

test('HTTPS, restrictive browser headers, canonical aliases and allowed methods are enforced', async () => {
  const worker = makeWorker();
  const http = await worker.fetch(new Request('http://example.com/?utm_source=sms'));
  assert.equal(http.status, 308);
  assert.equal(http.headers.get('Location'), 'https://example.com/?utm_source=sms');
  const main = await worker.fetch(request('/'));
  const policy = main.headers.get('Content-Security-Policy');
  assert.match(policy, /script-src 'self'/);
  assert.match(policy, /frame-ancestors 'none'/);
  assert.equal(policy.includes('unsafe-inline'), false);
  assert.equal(main.headers.get('X-Content-Type-Options'), 'nosniff');
  assert.equal(main.headers.get('X-Frame-Options'), 'DENY');
  assert.equal((await worker.fetch(request('/privacy'))).headers.get('Location'), site.origin + '/privacy/');
  assert.equal((await worker.fetch(request('/', { method: 'POST' }))).status, 405);
  const head = await worker.fetch(request('/', { method: 'HEAD' }));
  assert.equal(head.status, 200);
  assert.equal(await head.text(), '');
});

test('analytics is off by default and never creates application cookies', async () => {
  const points = [];
  const result = await makeWorker().fetch(request('/api/events', { method: 'POST' }), {
    ANALYTICS: { writeDataPoint: point => points.push(point) }
  });
  assert.equal(result.status, 204);
  assert.equal(points.length, 0);
  assert.equal(result.headers.has('Set-Cookie'), false);
});

test('opt-in aggregate analytics rejects cross-origin, oversized and malformed input and respects DNT/GPC', async () => {
  const points = [];
  const env = { ANALYTICS: { writeDataPoint: point => points.push(point) } };
  const enabled = { ...site, analytics: { enabled: true } };
  const worker = makeWorker(undefined, { site: enabled });
  const send = (body, extra = {}, origin = site.origin) => worker.fetch(request('/api/events', {
    method: 'POST', headers: { Origin: origin, 'Content-Type': 'application/json', ...extra }, body
  }), env);
  const body = JSON.stringify({ event: 'page_view', attribution: { utm_source: 'sms', utm_campaign: 'launch' }, ip: 'ignored' });
  assert.equal((await send(body, {}, 'https://other.example')).status, 403);
  assert.equal((await send('x'.repeat(2050))).status, 413);
  assert.equal((await send('{broken')).status, 400);
  assert.equal((await send(body, { DNT: '1' })).status, 204);
  assert.equal((await send(body, { 'Sec-GPC': '1' })).status, 204);
  assert.equal(points.length, 0);
  assert.equal((await send(body)).status, 204);
  assert.deepEqual(points, [{ indexes: ['page_view'], blobs: ['sms', '', 'launch', ''], doubles: [1] }]);
});

test('a failed optional metric cannot interrupt the download', async () => {
  const enabled = { ...site, analytics: { enabled: true } };
  const worker = makeWorker(async () => sourceResponse(), { site: enabled });
  const result = await worker.fetch(request('/download?utm_source=sms'), {
    ANALYTICS: { writeDataPoint() { throw new Error('metric service unavailable'); } }
  });
  assert.equal(result.status, 200);
  assert.equal(await result.text(), 'APK!');
});

// A frozen fingerprint from the previously approved version protects the visible presentation.
// Asset paths may be reorganized; text, markup, layout classes and original CSS stay the same.
test('the approved presentation body and original styles are preserved', async () => {
  const snapshot = JSON.parse(await readFile(new URL('./fixtures/presentation.json', import.meta.url)));
  const normalise = value => value.replace(/\/assets\/[^\s"'<>]+/g, '/assets/asset').replace(/\s+/g, ' ').replace(/>\s+</g, '><').trim();
  const hash = value => createHash('sha256').update(normalise(value)).digest('hex');
  const body = pages.index.split('<body>')[1].split('</body>')[0];
  // The small mocked release has a different size label; the visible app uses the real release.
  const actualBody = renderPages(site, actualRelease, { styles: '/assets/site.css', script: '/assets/app.js' }).index.split('<body>')[1].split('</body>')[0];
  assert.ok(body);
  assert.equal(hash(actualBody), snapshot.visibleBodySha256);
  const css = (await readFile(new URL('../src/styles/site.css', import.meta.url), 'utf8')).split('/* Standalone privacy/error documents;')[0];
  assert.equal(hash(css), snapshot.originalStylesSha256);
});
