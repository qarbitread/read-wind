import { readFileSync } from 'node:fs';
import { icon } from './icons.mjs';
import { renderPage as renderPresentation } from './presentation.mjs';

export const escapeHtml = (value = '') => String(value).replace(/[&<>"']/g, character => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
})[character]);
export const sizeLabel = bytes => `${(bytes / 1_000_000).toFixed(1)} MB`;
const jsonForHtml = value => JSON.stringify(value).replace(/</g, '\\u003c');
const readTemplate = name => readFileSync(new URL(`./templates/${name}.html`, import.meta.url), 'utf8');

function fill(template, values) {
  return template.replace(/\{\{([A-Z_]+)\}\}/g, (_, name) => {
    if (!(name in values)) throw new Error(`Template value missing: ${name}`);
    return values[name];
  });
}

export function renderPages(site, release, files) {
  const e = escapeHtml;
  const asset = path => files[path] || path;
  const size = sizeLabel(release.sizeBytes);
  const expand = text => text.replaceAll('{version}', release.version).replaceAll('{size}', size);
  const homeTitle = expand(site.title);
  const description = expand(site.description);
  const origin = site.origin;
  const validPublisher = site.publisherVerified && site.publisher;
  const brand = `<a class="brand" href="/" aria-label="JAIHO777 home"><img src="${asset(site.iconSmall)}" width="32" height="32" alt=""><span>JAIHO<span class="brand-number">777</span></span></a>`;
  const footer = `<footer class="site-footer"><div class="container footer-inner"><div><a class="brand footer-brand" href="/">JAIHO<span class="brand-number">777</span></a><p>Android APK download information.</p></div><nav class="footer-links" aria-label="Footer navigation"><a href="/privacy/">Privacy</a><a href="/#app-details">App details</a><span>18+ only</span></nav></div><p class="container footer-note">© ${site.updatedAt.slice(0, 4)} JAIHO777. Independent download page. Not affiliated with Google Play. Check the app’s terms and availability for your location.</p></footer>`;
  const schemas = [
    {
      '@context': 'https://schema.org', '@type': 'SoftwareApplication',
      name: site.name, operatingSystem: `Android ${release.minimumAndroid}+`,
      applicationCategory: 'GameApplication', softwareVersion: release.version,
      fileSize: `${release.sizeBytes} bytes`, contentRating: '18+',
      url: `${origin}/`, downloadUrl: `${origin}/download`, image: origin + asset(site.iconLarge),
      ...(validPublisher ? { publisher: { '@type': 'Organization', name: site.publisher } } : {})
    },
    { '@context': 'https://schema.org', '@type': 'WebSite', name: site.name, url: `${origin}/`, inLanguage: site.language }
  ];
  function head(title, path, text, indexable = true, home = false) {
    const canonical = origin + path;
    const socialImage = origin + asset(site.socialImage);
    return `<meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
      <title>${e(title)}</title><meta name="description" content="${e(text)}">
      <meta name="robots" content="${indexable ? 'index,follow,max-image-preview:large' : 'noindex,nofollow'}">
      <meta name="theme-color" content="#00875A"><meta name="color-scheme" content="light">
      <link rel="canonical" href="${e(canonical)}">
      <link rel="icon" href="${asset(site.favicon)}" sizes="any"><link rel="icon" type="image/png" href="${asset(site.faviconPng)}" sizes="32x32">
      <link rel="apple-touch-icon" href="${asset(site.appleIcon)}" sizes="180x180">
      <meta property="og:type" content="website"><meta property="og:locale" content="${e(site.locale)}">
      <meta property="og:site_name" content="${e(site.name)}"><meta property="og:title" content="${e(title)}">
      <meta property="og:description" content="${e(text)}"><meta property="og:url" content="${e(canonical)}">
      <meta property="og:image" content="${e(socialImage)}"><meta property="og:image:secure_url" content="${e(socialImage)}">
      <meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:type" content="image/jpeg"><meta property="og:image:alt" content="JAIHO777 Android APK download">
      <meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="${e(title)}"><meta name="twitter:description" content="${e(text)}"><meta name="twitter:image" content="${e(socialImage)}">
      <link rel="preload" href="${asset('/assets/fonts/roboto-regular.woff2')}" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="${files.styles}">
      ${home ? `<script type="application/ld+json">${jsonForHtml(schemas)}</script><script id="page-config" type="application/json">${jsonForHtml(publicConfig)}</script><script src="${files.script}" defer></script>` : ''}`;
  }
  const presentationConfig = {
    ...site, apk: release, icon: asset(site.icon),
    screenshots: site.screenshots.map(image => ({ ...image, src: asset(image.src), thumbnailSrc: asset(image.thumbnailSrc) })),
    promoBanner: site.promoBanner?.enabled ? {
      ...site.promoBanner,
      image: asset(site.promoBanner.image)
    } : site.promoBanner,
    demoPresentation: {
      ...site.demoPresentation,
      reviews: (site.demoPresentation?.reviews || []).map(review => ({ ...review, avatar: asset(review.avatar) }))
    }
  };
  const original = renderPresentation(presentationConfig).replaceAll('/assets/play-store-demo.webp', asset(site.playStoreIcon));
  const body = original.slice(original.indexOf('<body>') + '<body>'.length, original.lastIndexOf('</body>'));
  const publicConfig = JSON.parse(original.match(/<script type="application\/json" id="page-config">([\s\S]*?)<\/script>/)[1]);
  const icons = Object.fromEntries(['help', 'android', 'arrow', 'back', 'check', 'info', 'plus', 'phone', 'close'].map(name => [`ICON_${name.toUpperCase()}`, icon(name)]));
  const common = {
    ...icons, LANGUAGE: e(site.language), BRAND: brand, FOOTER: footer,
    APP_ICON: asset(site.icon), SMALL_ICON: asset(site.iconSmall), SIZE: size,
    SIZE_BYTES: release.sizeBytes.toLocaleString('en-US'), VERSION: e(release.version), ANDROID: e(release.minimumAndroid),
    FILENAME: e(release.filename), PACKAGE: e(release.packageName), CHECKSUM: e(release.sha256),
    SUPPORT_HANDLE: e(site.supportHandle), UPDATED_DATE: e(site.updatedAt), ATTRIBUTION_TTL: site.attribution.ttlMinutes,
    ANALYTICS_NOTICE: site.analytics.enabled
      ? 'Optional aggregate website metrics are enabled. Browser privacy preferences are respected.'
      : 'Analytics collection is currently disabled. No advertising pixels or third-party analytics scripts are loaded.'
  };
  const index = fill(readTemplate('index'), {
    LANGUAGE: e(site.language), HEAD: head(homeTitle, '/', description, true, true), BODY: body
  });
  const privacy = fill(readTemplate('privacy'), {
    ...common, HEAD: head('Website privacy notice | JAIHO777', '/privacy/', 'How the JAIHO777 APK download website handles campaign labels, browser storage and optional website metrics.')
  });
  const error = (code, title, message) => fill(readTemplate('error'), {
    ...common, HEAD: head(`${title} | JAIHO777`, '/', message, false),
    ERROR_CODE: String(code), ERROR_TITLE: e(title), ERROR_MESSAGE: e(message)
  });
  return {
    index, privacy,
    robots: `User-agent: *\nAllow: /\nDisallow: /download\nDisallow: /api/\n\nSitemap: ${origin}/sitemap.xml\n`,
    sitemap: `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>${e(origin)}/</loc><lastmod>${site.updatedAt}</lastmod></url>\n  <url><loc>${e(origin)}/privacy/</loc><lastmod>${site.updatedAt}</lastmod></url>\n</urlset>\n`,
    notFound: error(404, 'Page not found', 'The page you requested is not available. Return to the app page for download information.'),
    downloadError: error(503, 'Download temporarily unavailable', 'Check your connection and try again in a moment.')
  };
}
