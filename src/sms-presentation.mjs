import { escapeHtml, sizeLabel } from './presentation.mjs';

export function renderSmsPage(config) {
  const e = escapeHtml;
  const a = config.apk;
  const fileSize = sizeLabel(a.sizeBytes);
  const withdraw = config.screenshots.find(item => /withdraw/i.test(item.title + item.caption + item.src)) || config.screenshots[config.screenshots.length - 1];
  const downloadHref = e(a.url);
  const download = (placement) => `<a class="sms-cta" href="${downloadHref}" download="${e(a.filename)}" data-download data-placement="${placement}" rel="noopener"><span class="sms-cta-label">Install APK</span><span class="sms-cta-meta">${fileSize} · Android</span></a>`;
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
<meta name="theme-color" content="#0B3D2E">
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
<div class="sms-atmosphere" aria-hidden="true"></div>
<header class="sms-top">
  <p class="sms-brand">JAIHO<span>777</span></p>
  <p class="sms-channel">Android APK · India</p>
</header>
<main id="sms-main" class="sms-shell">
  <section class="sms-hero" aria-labelledby="sms-title">
    <div class="sms-copy">
      <p class="sms-kicker">Official download</p>
      <h1 id="sms-title">Withdraw to your bank in minutes</h1>
      <p class="sms-lede">Install JAIHO777 on Android, pay with UPI, and cash out to your Indian bank account.</p>
      ${download('sms-hero')}
      <p class="sms-fine">Direct APK · No Play Store redirect · 18+</p>
    </div>
    <div class="sms-visual">
      <figure class="sms-phone">
        <img src="${e(withdraw.src)}" width="${withdraw.width}" height="${withdraw.height}" alt="${e(withdraw.alt)}" fetchpriority="high" decoding="async">
      </figure>
    </div>
  </section>
  <section class="sms-flow" aria-labelledby="sms-flow-title">
    <h2 id="sms-flow-title">From SMS to payout</h2>
    <p class="sms-flow-intro">Three short steps. Built for phones in India.</p>
    <ol class="sms-steps">
      <li><strong>Install</strong><span>Save the official APK and open it.</span></li>
      <li><strong>Play with UPI</strong><span>Sign in with your mobile number and deposit.</span></li>
      <li><strong>Withdraw</strong><span>Send winnings to your bank. Track status in the app.</span></li>
    </ol>
  </section>
</main>
<footer class="sms-foot">
  <p><strong>JAIHO777</strong> official APK page for SMS traffic. Not affiliated with Google Play.</p>
  <p><a href="/">Play Store listing</a> · <a href="/privacy/">Privacy</a> · ${e(a.version)} · ${fileSize}</p>
</footer>
<p id="download-status" class="sms-sr" role="status" aria-live="polite"></p>
</body>
</html>`;
}
