import { escapeHtml, sizeLabel } from './presentation.mjs';

export function renderSmsPage(config) {
  const e = escapeHtml;
  const a = config.apk;
  const fileSize = sizeLabel(a.sizeBytes);
  const withdraw = config.screenshots.find(item => /withdraw/i.test(item.title + item.caption + item.src)) || config.screenshots[config.screenshots.length - 1];
  const logo = config.smsLogo || config.icon;
  const downloadHref = e(a.url);
  const action = (label, placement, className) => (
    `<a class="sms-btn ${className}" href="${downloadHref}" download="${e(a.filename)}" data-download data-placement="${placement}" rel="noopener">` +
    `<span class="sms-btn-shine" aria-hidden="true"></span><span class="sms-btn-label">${label}</span></a>`
  );
  const publicConfig = {
    analytics: config.analytics,
    attribution: config.attribution,
    downloadUrl: a.url
  };
  const json = JSON.stringify(publicConfig).replace(/</g, '\\u003c');
  const structuredData = JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'SoftwareApplication',
    name: config.name,
    operatingSystem: `Android ${a.minimumAndroid}+`,
    applicationCategory: 'GameApplication',
    softwareVersion: a.version,
    fileSize: `${a.sizeBytes} bytes`,
    contentRating: '18+',
    url: `${config.origin}/sms/`,
    downloadUrl: a.url,
    image: `${config.origin}${config.icon}`
  }).replace(/</g, '\\u003c');

  return `<!doctype html>
<html lang="en-IN" class="sms-root">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>JAIHO777 – Withdraw to Bank on Android</title>
<meta name="description" content="Install JAIHO777 on Android. Pay with UPI and withdraw winnings fast to your Indian bank account.">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#05261c">
<meta name="color-scheme" content="dark">
<link rel="canonical" href="${e(config.origin)}/sms/">
<link rel="icon" href="${e(config.favicon)}" sizes="any">
<link rel="icon" type="image/png" href="${e(config.faviconPng)}" sizes="32x32">
<link rel="apple-touch-icon" href="${e(config.appleIcon)}" sizes="180x180">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_IN">
<meta property="og:site_name" content="JAIHO777">
<meta property="og:title" content="JAIHO777 – Withdraw to Bank on Android">
<meta property="og:description" content="Official Android APK for India. UPI deposit. Fast bank withdrawals.">
<meta property="og:url" content="${e(config.origin)}/sms/">
<meta property="og:image" content="${e(config.origin)}${e(config.socialImage)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="JAIHO777 – Withdraw to Bank on Android">
<meta name="twitter:description" content="Official Android APK for India. UPI deposit. Fast bank withdrawals.">
<meta name="twitter:image" content="${e(config.origin)}${e(config.socialImage)}">
<link rel="preload" href="${e(config.fontFraunces)}" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="${e(config.fontSora)}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="${e(config.smsStyles)}">
<script type="application/ld+json">${structuredData}</script>
<script id="page-config" type="application/json">${json}</script>
<script src="${e(config.smsScript)}" defer></script>
</head>
<body class="sms-body">
<a class="sms-skip" href="#sms-main">Skip to content</a>
<main id="sms-main" class="sms-shell">
  <section class="sms-stage" aria-label="JAIHO777 SMS download">
    <h1 class="sms-sr">JAIHO777</h1>
    <div class="sms-topbar">
      ${action('REGISTER', 'sms-register', 'sms-btn-register')}
      ${action('PLAY NOW', 'sms-play', 'sms-btn-play')}
    </div>
    <figure class="sms-screen">
      <a class="sms-logo" href="${downloadHref}" download="${e(a.filename)}" data-download data-placement="sms-logo" rel="noopener" aria-label="JAIHO777">
        <img src="${e(logo)}" width="72" height="72" alt="JAIHO777" decoding="async" fetchpriority="high">
      </a>
      <img class="sms-screen-img" src="${e(withdraw.src)}" width="${withdraw.width}" height="${withdraw.height}" alt="${e(withdraw.alt)}" decoding="async" fetchpriority="high">
    </figure>
    <div class="sms-bottom">
      ${action('DOWNLOAD APK', 'sms-download', 'sms-btn-download')}
      <p class="sms-meta">${fileSize} · Android · 18+</p>
    </div>
  </section>
</main>
<p id="download-status" class="sms-sr" role="status" aria-live="polite"></p>
</body>
</html>`;
}
