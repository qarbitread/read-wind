import { streamApk } from './download.mjs';
import { collectAttribution, privacyOptOut, readSmallJson, recordEvent } from './attribution.mjs';

export const securityHeaders = {
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'X-Frame-Options': 'DENY',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=(), payment=(), browsing-topics=()',
  'Strict-Transport-Security': 'max-age=31536000',
  'Content-Security-Policy': "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'"
};
const htmlEscape = value => String(value).replaceAll('&', '&amp;').replaceAll('"', '&quot;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');

export function createWorker({ site, release, assets, pages, fetchImpl = (...args) => fetch(...args) }) {
  const response = (body, status = 200, headers = {}) => new Response(body, {
    status, headers: { ...securityHeaders, ...headers }
  });
  const htmlResponse = (request, body, status = 200, headers = {}) => response(request.method === 'HEAD' ? null : body, status, {
    'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'public, max-age=300, must-revalidate', ...headers
  });

  return {
    async fetch(request, env = {}) {
      const url = new URL(request.url);
      const path = url.pathname;
      if (url.protocol === 'http:' && !['localhost', '127.0.0.1', '0.0.0.0'].includes(url.hostname)) {
        url.protocol = 'https:';
        return response(null, 308, { Location: url.href });
      }
      if (url.href.length > 4096) return response('Request URL is too long.', 414, { 'Cache-Control': 'no-store' });

      if (path === '/api/events') {
        if (request.method !== 'POST') return response(null, 405, { Allow: 'POST' });
        if (!site.analytics.enabled || privacyOptOut(request)) return response(null, 204, { 'Cache-Control': 'no-store' });
        if (request.headers.get('Origin') !== url.origin) return response(null, 403);
        if (!request.headers.get('Content-Type')?.startsWith('application/json')) return response(null, 415);
        const body = await readSmallJson(request);
        if (body.status) return response(null, body.status);
        if (body.value?.event === 'page_view') {
          recordEvent(request, env, site, 'page_view', collectAttribution(body.value.attribution, site.attribution));
        }
        return response(null, 204, { 'Cache-Control': 'no-store' });
      }
      if (!['GET', 'HEAD'].includes(request.method)) return response(null, 405, { Allow: 'GET, HEAD' });

      if (path === '/download') {
        const file = await streamApk(request, release, fetchImpl);
        if (file.error === 416) return response(null, 416, { ...file.headers, 'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex' });
        if (file.error) {
          // Upstream proxy can fail at the edge; fall back to the fixed HTTPS APK URL
          // so Install/Download buttons still deliver the file (labels stay on /download only).
          return response(null, 302, {
            Location: release.url,
            'Cache-Control': 'no-store',
            'X-Robots-Tag': 'noindex',
            'Retry-After': '60'
          });
        }
        if (request.method === 'GET') {
          recordEvent(request, env, site, 'download_request', collectAttribution(url.searchParams, site.attribution));
        }
        return response(file.body, file.status, file.headers);
      }

      if (path === '/index.html' || path === '/privacy' || path === '/privacy/index.html' || path === '/sms' || path === '/sms/index.html') {
        url.pathname = path === '/index.html' ? '/' : path.startsWith('/sms') ? '/sms/' : '/privacy/';
        return response(null, 301, { Location: url.href, 'Cache-Control': 'public, max-age=3600' });
      }
      const withApkAttribution = (html) => {
        const labels = new URLSearchParams(collectAttribution(url.searchParams, site.attribution)).toString();
        const apkHref = 'href="/download"';
        const page = labels ? html.replaceAll(apkHref, `href="/download?${htmlEscape(labels)}"`) : html;
        return { page, labels };
      };
      if (path === '/') {
        const { page, labels } = withApkAttribution(pages.index);
        return htmlResponse(request, page, 200, labels ? { 'Cache-Control': 'private, no-store' } : {});
      }
      if (path === '/sms/') {
        const { page, labels } = withApkAttribution(pages.sms);
        return htmlResponse(request, page, 200, labels ? { 'Cache-Control': 'private, no-store' } : {});
      }
      if (path === '/privacy/') return htmlResponse(request, pages.privacy);
      if (path === '/robots.txt' || path === '/sitemap.xml') {
        const sitemap = path === '/sitemap.xml';
        return response(request.method === 'HEAD' ? null : pages[sitemap ? 'sitemap' : 'robots'], 200, {
          'Content-Type': sitemap ? 'application/xml; charset=utf-8' : 'text/plain; charset=utf-8',
          'Cache-Control': 'public, max-age=3600'
        });
      }

      // Only this generated public-asset allowlist is served. Source/config files have no route.
      const asset = assets[path];
      if (asset) {
        const cache = asset.immutable ? 'public, max-age=31536000, immutable' : 'public, max-age=86400, must-revalidate';
        if (request.headers.get('If-None-Match') === asset.etag) return response(null, 304, { ETag: asset.etag, 'Cache-Control': cache });
        const headers = { 'Content-Type': asset.type, 'Cache-Control': cache, ETag: asset.etag, 'Content-Length': String(asset.size) };
        if (request.method === 'HEAD') return response(null, 200, headers);
        const bytes = Uint8Array.from(atob(asset.base64), character => character.charCodeAt(0));
        return response(bytes, 200, headers);
      }
      return htmlResponse(request, pages.notFound, 404, { 'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex' });
    }
  };
}
