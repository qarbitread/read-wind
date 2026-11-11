import { escapeHtml, sizeLabel } from './presentation.mjs';

export function renderSmsPage(config) {
  const e = escapeHtml;
  const a = config.apk;
  const fileSize = sizeLabel(a.sizeBytes);
  const withdraw = config.screenshots.find(item => /withdraw/i.test(item.title + item.caption + item.src)) || config.screenshots[config.screenshots.length - 1];
  const lobby = config.screenshots.find(item => /lobby|game lobby/i.test(item.title + item.caption + item.src)) || config.screenshots[3] || withdraw;
  const downloadHref = e(a.url);
  const download = (placement, extra = '') => `<a class="sms-cta ${extra}" href="${downloadHref}" download="${e(a.filename)}" data-download data-placement="${placement}" rel="noopener"><span class="sms-cta-main">Install APK</span><span class="sms-cta-sub">${fileSize} · Android · India</span></a>`;
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
<meta name="theme-color" content="#041910">
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
<div class="sms-atmosphere" aria-hidden="true">
  <span class="sms-orb sms-orb-a"></span>
  <span class="sms-orb sms-orb-b"></span>
  <span class="sms-orb sms-orb-c"></span>
  <span class="sms-sheen"></span>
</div>
<main id="sms-main">
  <section class="sms-hero" aria-labelledby="sms-brand">
    <div class="sms-hero-copy">
      <p class="sms-mark">Official APK for India</p>
      <h1 id="sms-brand" class="sms-brand">JAIHO<span>777</span></h1>
      <p class="sms-headline">Withdraw to your bank in minutes</p>
      <p class="sms-lede">Pay with UPI. Cash out to SBI, HDFC, and more. Built for Android phones in India.</p>
      ${download('sms-hero')}
      <p class="sms-fine">Direct download · No Play Store redirect · 18+</p>
    </div>
    <div class="sms-hero-stage" aria-hidden="false">
      <figure class="sms-stage-main">
        <img src="${e(withdraw.src)}" width="${withdraw.width}" height="${withdraw.height}" alt="${e(withdraw.alt)}" fetchpriority="high" decoding="async">
      </figure>
      <figure class="sms-stage-side">
        <img src="${e(lobby.src)}" width="${lobby.width}" height="${lobby.height}" alt="${e(lobby.alt)}" loading="lazy" decoding="async">
      </figure>
    </div>
  </section>

  <section class="sms-flow" aria-labelledby="sms-flow-title">
    <div class="sms-flow-head">
      <h2 id="sms-flow-title">From SMS link to bank credit</h2>
      <p>Three moves. No long form.</p>
    </div>
    <ol class="sms-rail">
      <li><span class="sms-num">01</span><div><strong>Install</strong><p>Tap Install APK and open the file on your phone.</p></div></li>
      <li><span class="sms-num">02</span><div><strong>Pay with UPI</strong><p>Sign in with your mobile number and deposit.</p></div></li>
      <li><span class="sms-num">03</span><div><strong>Withdraw</strong><p>Send winnings to your bank. Watch status turn Succeed.</p></div></li>
    </ol>
  </section>
</main>
<footer class="sms-foot">
  <p><strong>JAIHO777</strong> SMS download page. Not affiliated with Google Play.</p>
  <p><a href="/">Play Store listing</a> · <a href="/privacy/">Privacy</a> · ${e(a.version)} · ${fileSize}</p>
</footer>
<div class="sms-sticky" aria-label="Quick install">${download('sms-sticky', 'sms-cta-sticky')}</div>
<p id="download-status" class="sms-sr" role="status" aria-live="polite"></p>
</body>
</html>`;
}
