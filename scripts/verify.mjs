import assert from 'node:assert/strict';
import { readFile, readdir, stat } from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const root = path.resolve(import.meta.dirname, '..');
const dist = path.join(root, 'dist');
const read = file => readFile(path.join(dist, file), 'utf8');
const report = JSON.parse(await read('reports/build-report.json'));
const release = JSON.parse(await readFile(path.join(root, 'config/release.json'), 'utf8'));
const index = await read('public/index.html');
const privacy = await read('public/privacy/index.html');
const sitemap = await read('public/sitemap.xml');
const robots = await read('public/robots.txt');
const checks = [];
const check = (name, action) => { action(); checks.push(name); };

check('one H1 and complete English Android listing', () => {
  assert.equal((index.match(/<h1\b/g) || []).length, 1);
  assert.match(index, /<html lang="en-IN">/);
  assert.ok(index.includes('India.<br class="desktop-break"> Download'), 'Preserve word spacing when the desktop line break is hidden on mobile');
  assert.match(index, /<title>JAIHO777 APK for Android – Download &amp; Play in India<\/title>/);
  assert.match(index, /name="description" content="[^\"]{90,180}"/);
  assert.match(index, /name="robots" content="index,follow/);
  assert.match(index, /JAIHO777 Games/);
  assert.match(index, /18\.6K reviews/);
  assert.match(index, /Google Play/);
  assert.match(index, /realcashgame\.app/);
  assert.equal(/Works on Jio/.test(index), false);
  assert.equal(/button-size/.test(index), false);
});
check('canonical, Open Graph and sitemap share the configured HTTPS origin', () => {
  assert.match(index, new RegExp(`<link rel="canonical" href="${report.origin}/">`));
  assert.equal(index.includes(`property="og:url" content="${report.origin}/"`), true);
  assert.equal(index.includes(`property="og:image" content="${report.origin}/assets/brand/`), true);
  assert.equal(privacy.includes(`rel="canonical" href="${report.origin}/privacy/"`), true);
  const locations = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map(match => match[1]);
  assert.deepEqual(locations, [report.origin + '/', report.origin + '/sms/', report.origin + '/privacy/']);
  assert.equal(robots.includes(`Sitemap: ${report.origin}/sitemap.xml`), true);
  assert.equal(robots.includes('Disallow: /download'), true);
  assert.equal(robots.includes('Allow: /'), true);
});
const sms = await read('public/sms/index.html');
check('SMS landing uses withdrawal screen with Register, Play Now and Download APK', () => {
  assert.equal((sms.match(/<h1\b/g) || []).length, 1);
  assert.match(sms, /REGISTER/);
  assert.match(sms, /PLAY NOW/);
  assert.match(sms, /DOWNLOAD APK/);
  assert.match(sms, /sms-btn-register/);
  assert.match(sms, /sms-btn-play/);
  assert.match(sms, /sms-btn-download/);
  assert.match(sms, /sms-logos/);
  assert.equal((sms.match(/class="sms-logo"/g) || []).length, 2);
  assert.equal((sms.match(new RegExp(`href="${release.url.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}"`, 'g')) || []).length >= 4, true);
  assert.match(sms, new RegExp(`<link rel="canonical" href="${report.origin}/sms/">`));
  assert.equal(sms.includes('Google Play</span>'), false);
});
check('seven supplied screens, withdrawals banner, lazy thumbnails and factual structured data', () => {
  assert.equal((index.match(/data-gallery=/g) || []).length, 7);
  assert.ok((index.match(/loading="lazy"/g) || []).length >= 6);
  const schemas = JSON.parse(index.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1]);
  assert.equal(schemas[0].softwareVersion, release.version);
  assert.equal(schemas[0].fileSize, `${release.sizeBytes} bytes`);
  assert.equal('aggregateRating' in schemas[0], false);
  const runtime = JSON.parse(index.match(/<script id="page-config" type="application\/json">([\s\S]*?)<\/script>/)[1]);
  assert.equal(runtime.analytics.enabled, false);
  assert.equal(runtime.gallery.length, 7);
  assert.equal(runtime.gallery[0].title, 'Welcome to JAIHO777');
  assert.equal(runtime.gallery[5].title, 'Promotions & VIP');
  assert.equal(runtime.gallery[6].title, 'Fast withdrawals');
  assert.equal(/promo-banner/.test(index), false);
  assert.equal(/Aarav Sharma/.test(index), true);
  assert.equal(/Priya Patel/.test(index), true);
  assert.equal(/Vikram Singh/.test(index), true);
  assert.equal(/people found this review helpful/.test(index), true);
  assert.equal(/DEMO/.test(index), false);
  assert.equal(/Fictional/.test(index), false);
  assert.equal(/Verified App/.test(index), true);
  assert.equal(/Ratings and reviews/.test(index), true);
  assert.equal(/favourite money game/.test(index), true);
});
check('small browser payload and no third-party scripts or source maps', () => {
  assert.ok(report.html.gzipBytes < 15000);
  assert.ok(report.css.bytes < 32000);
  assert.ok(report.javascript.bytes < 10000);
  assert.ok(report.thumbnailBytes < 400000);
  assert.equal(report.thirdPartyBrowserScripts, 0);
  assert.equal(report.sourceMaps, false);
  assert.equal(/<script[^>]+src="https?:/i.test(index), false);
});

const allFiles = [];
async function walk(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const filename = path.join(directory, entry.name);
    if (entry.isDirectory()) await walk(filename);
    else allFiles.push(filename);
  }
}
await walk(path.join(dist, 'public'));
check('public export excludes source, configuration, repositories and APK copies', () => {
  for (const file of allFiles) {
    const relative = path.relative(path.join(dist, 'public'), file);
    assert.equal(/(^|\/)(config|src|node_modules|\.git|\.openai)(\/|$)|\.map$|\.apk$|package(?:-lock)?\.json$/.test(relative), false, relative);
  }
});
for (const file of allFiles.filter(file => /\.(html|js|css|xml|txt)$/.test(file))) {
  const text = await readFile(file, 'utf8');
  assert.equal(text.includes('sourceMappingURL'), false, file);
  assert.equal(text.includes('{{'), false, file);
}
const indexHtml = await readFile(path.join(dist, 'public', 'index.html'), 'utf8');
assert.equal(indexHtml.includes(`href="${release.url}"`), true, 'Install buttons must point at the release APK URL');
assert.equal((indexHtml.match(new RegExp(`href="${release.url.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}"`, 'g')) || []).length >= 2, true);
checks.push('Install buttons use the direct release APK URL with no unresolved placeholders');
for (const url of Object.values(report.assetManifest)) await stat(path.join(dist, 'public', url));
checks.push('every hashed browser asset exists');

const worker = (await import(pathToFileURL(path.join(dist, 'server/index.js')).href)).default;
for (const route of ['/', '/sms/', '/privacy/', '/robots.txt', '/sitemap.xml', ...Object.values(report.assetManifest)]) {
  const response = await worker.fetch(new Request(report.origin + route, { method: 'HEAD' }));
  assert.equal(response.status, 200, route);
  assert.equal(response.headers.get('X-Content-Type-Options'), 'nosniff', route);
}
checks.push('built Worker serves all public pages and hashed assets');
{
  const ok = await worker.fetch(new Request(report.origin + '/download', {
    method: 'HEAD',
    redirect: 'manual'
  }));
  assert.equal([200, 302].includes(ok.status), true, `/download status ${ok.status}`);
  if (ok.status === 302) assert.equal(ok.headers.get('Location'), release.url);
}
checks.push('built Worker /download streams or falls back to the fixed APK URL');
for (const route of ['/src/render.mjs', '/config/release.json', '/.git/config', '/.env', '/package.json', '/assets/app.js.map', '/__qa/mobile']) {
  const response = await worker.fetch(new Request(report.origin + route));
  assert.equal(response.status, 404, route);
}
checks.push('built Worker blocks private paths and preview fixtures');
console.log(`Verified ${checks.length} production requirements and ${Object.keys(report.assetManifest).length} browser asset references.`);
for (const name of checks) console.log(`✓ ${name}`);
