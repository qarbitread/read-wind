export const escapeHtml = (value = '') => String(value).replace(/[&<>"']/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[ch]);
export const sizeLabel = bytes => `${(bytes / 1000000).toFixed(1)} MB`;
const icon = (name, cls = '') => `<svg class="icon ${cls}" aria-hidden="true"><use href="#i-${name}"></use></svg>`;
const symbols = `<svg class="symbols" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><defs>
<symbol id="i-download" viewBox="0 0 24 24"><path d="M12 3v12m-4-4 4 4 4-4M5 16v4h14v-4"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="m9 5 7 7-7 7"/></symbol>
<symbol id="i-back" viewBox="0 0 24 24"><path d="m15 5-7 7 7 7"/></symbol>
<symbol id="i-expand" viewBox="0 0 24 24"><path d="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5"/></symbol>
<symbol id="i-close" viewBox="0 0 24 24"><path d="m6 6 12 12M6 18 18 6"/></symbol>
<symbol id="i-android" viewBox="0 0 24 24"><path d="m7 3 2 3m8-3-2 3M5 12a7 7 0 0 1 14 0v6H5v-6Zm3 6v3m8-3v3M2 12v5m20-5v5"/><path d="M9 10h.01M15 10h.01"/></symbol>
<symbol id="i-file" viewBox="0 0 24 24"><path d="M14 3H5v18h14V8l-5-5Zm0 0v5h5M9 13h6m-6 4h6"/></symbol>
<symbol id="i-help" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9.7 8.3a2.5 2.5 0 0 1 4.6 1.3c0 1.7-2.3 2.1-2.3 3.9M12 17h.01"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="m5 12 4 4L19 6"/></symbol>
<symbol id="i-info" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 11v6m0-10h.01"/></symbol>
<symbol id="i-plus" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><rect x="6" y="2" width="12" height="20" rx="2"/><path d="M10 18h4"/></symbol>
</defs></svg>`;

export function galleryImage(item, index, fullscreen = false) {
  const common = `alt="${escapeHtml(item.alt)}" decoding="async" ${fullscreen ? '' : `loading="${index ? 'lazy' : 'eager'}"`}`;
  if (item.sourceWidth) {
    const w = item.sourceWidth / item.width * 100;
    const left = -item.cropX / item.width * 100;
    const top = -item.cropY / item.height * 100;
    return `<span class="art-crop" style="aspect-ratio:${item.width}/${item.height}"><img src="${escapeHtml(item.src)}" width="${item.sourceWidth}" height="${item.sourceHeight}" style="width:${w}%;left:${left}%;top:${top}%" ${common}></span>`;
  }
  const source = !fullscreen && item.thumbnailSrc ? item.thumbnailSrc : item.src;
  return `<img class="screen-image" src="${escapeHtml(source)}" width="${item.width}" height="${item.height}" ${common}>`;
}

export function renderPage(config) {
  const e = escapeHtml, a = config.apk, fileSize = sizeLabel(a.sizeBytes);
  const hasScreenshots = config.screenshots.length > 0;
  const gallery = hasScreenshots ? config.screenshots : config.artwork;
  const downloadHref = e(a.url);
  const download = (location, extra = '') => `<a class="download-button ${extra}" href="${downloadHref}" download="${e(a.filename)}" data-download data-placement="${location}" rel="noopener">${icon('download')}<span>Install</span></a>`;
  const publicConfig = {
    analytics: config.analytics, attribution: config.attribution,
    downloadUrl: a.url,
    gallery: gallery.map((item, i) => ({title:item.title,html:galleryImage(item, i, true)}))
  };
  const json = JSON.stringify(publicConfig).replace(/</g, '\\u003c');
  const structuredData = JSON.stringify({
    '@context':'https://schema.org','@type':'SoftwareApplication',name:config.name,
    operatingSystem:`Android ${a.minimumAndroid}+`,applicationCategory:'GameApplication',
    softwareVersion:a.version,fileSize:`${a.sizeBytes} bytes`,contentRating:'18+',
    url:config.origin,downloadUrl:a.url,image:`${config.origin}${config.icon}`,
    ...(config.publisherVerified && config.publisher ? {publisher:{'@type':'Organization',name:config.publisher}} : {})
  }).replace(/</g, '\\u003c');
  const publisher = config.publisherVerified && config.publisher;
  const store = config.demoPresentation?.enabled === true;
  const headerBrand = store
    ? '<a class="brand play-store-brand" href="/" aria-label="Google Play"><img src="/assets/play-store-demo.webp" width="32" height="32" alt=""><span>Google Play</span></a>'
    : `<a class="brand" href="/" aria-label="JAIHO777 home"><img src="${e(config.icon)}" width="32" height="32" alt=""><span>JAIHO<span class="brand-number">777</span></span></a>`;
  const storeMeta = config.demoPresentation || {};
  const reviews = store ? storeMeta.reviews || [] : [];
  const reviewsHtml = reviews.length ? `<section id="ratings-reviews" class="app-reviews section-block" aria-labelledby="ratings-reviews-heading"><div class="section-heading"><div><h2 id="ratings-reviews-heading">Ratings and reviews</h2><p class="reviews-summary">${e(storeMeta.ratingCountLabel || '18.6K reviews')} from players in India</p></div></div><div class="review-list">${reviews.map((review,index)=>{
    const stars = Math.max(1,Math.min(5,Math.round(Number(review.rating)||5)));
    const when = e(review.posted || '');
    const device = e(review.device || '');
    const helpful = Number(review.helpful) > 0 ? Number(review.helpful).toLocaleString('en-IN') : '';
    const avatar = review.avatar
      ? `<img class="review-avatar" src="${e(review.avatar)}" width="44" height="44" loading="lazy" decoding="async" alt="${e(review.name)}">`
      : `<span class="review-avatar review-initials" aria-hidden="true">${e(review.initials || review.name.slice(0,2).toUpperCase())}</span>`;
    return `<article class="app-review" aria-labelledby="review-${index}"><header class="review-header">${avatar}<div class="review-person"><h3 id="review-${index}">${e(review.name)}</h3><p>${[when, device].filter(Boolean).join(' · ')}</p></div></header><div class="review-rating"><span class="review-stars" role="img" aria-label="Rated ${stars} out of 5">${'★'.repeat(stars)}${'☆'.repeat(5-stars)}</span><span>${stars}.0</span></div><blockquote><p>${e(review.comment)}</p></blockquote>${helpful ? `<p class="review-helpful">${helpful} people found this review helpful</p>` : ''}</article>`;
  }).join('')}</div></section>` : '';
  const verifiedBadge = `<span class="verified-badge" aria-label="Verified App"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 2 8 4v6c0 4-4 8-8 10-4-2-8-6-8-10V6l8-4Z"/><path d="m8 11 3 3 5-5"/></svg><span>Verified App</span></span>`;
  const ratingValue = e(storeMeta.ratingValue || '4.8');
  const downloadsLabel = e(storeMeta.downloadsLabel || '5M+');
  const appStats = `<div class="app-stats" aria-label="App rating and downloads"><div><strong>${ratingValue} <span class="rating-star" aria-hidden="true">★</span></strong><span>${e(storeMeta.ratingCountLabel || '18.6K reviews')}</span></div><div><strong>${downloadsLabel}</strong><span>Downloads</span></div><div><strong><span class="real-age">18+</span></strong><span>Rated for 18+</span></div></div>`;
  const bannerHtml = '';
  return `<!doctype html>
<html lang="en-IN"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>${e(config.title)}</title><meta name="description" content="${e(config.description)}">
<meta name="theme-color" content="#00875A"><meta name="color-scheme" content="light">
<link rel="canonical" href="${e(config.origin)}/"><link rel="icon" type="image/webp" href="${e(config.icon)}"><link rel="apple-touch-icon" href="${e(config.icon)}">
<meta property="og:type" content="website"><meta property="og:locale" content="en_IN"><meta property="og:site_name" content="JAIHO777">
<meta property="og:title" content="${e(config.title)}"><meta property="og:description" content="${e(config.description)}"><meta property="og:url" content="${e(config.origin)}/">
<meta property="og:image" content="${e(config.origin)}${e(config.socialImage)}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="JAIHO777 Android APK direct download">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="${e(config.title)}"><meta name="twitter:description" content="${e(config.description)}"><meta name="twitter:image" content="${e(config.origin)}${e(config.socialImage)}">
<link rel="preload" href="/assets/roboto-regular.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/styles.css?v=${e(config.assetVersion||'1')}">
<script type="application/ld+json">${structuredData}</script><script type="application/json" id="page-config">${json}</script><script src="/app.js?v=${e(config.assetVersion||'1')}" defer></script>
</head><body>${symbols}
<a class="skip-link" href="#main">Skip to app information</a>
<header class="site-header"><div class="header-inner">
${headerBrand}
<nav class="top-nav" aria-label="Main navigation"><a href="#about">About</a><a href="#install">Install</a><a href="#help">Help ${icon('help')}</a></nav>
<span class="header-label">Apps &amp; games</span>
</div></header>
<main id="main" class="page-wrap">
<div class="breadcrumb"><span>Games</span>${icon('arrow')}<span>Casino</span>${icon('arrow')}<span class="breadcrumb-current">JAIHO777</span></div>
<section class="app-hero" aria-labelledby="app-title">
<div class="app-overview"><div class="app-identity"><img class="app-icon" src="${e(config.icon)}" alt="JAIHO777 app icon" width="140" height="140" fetchpriority="high"><div class="identity-text"><h1 id="app-title">JAIHO777</h1><p class="publisher-line">${publisher ? e(publisher) : 'JAIHO777 Games'}</p><p class="app-category">Casino <span>·</span> Contains ads <span>·</span> In-app purchases</p>${store ? verifiedBadge : ''}</div></div>
<p class="hero-description">JAIHO777 is a favourite money game in India.<br class="desktop-break"> Download on Android, play slots, arcade and fishing, pay with UPI, and withdraw fast to your bank.</p>
${store ? appStats : ''}
</div>
<aside class="download-panel" aria-label="Install JAIHO777"><div class="download-panel-top"><span class="android-label">${icon('android')} Android</span><span class="version-label">${e(a.version)}</span></div><h2>Install</h2><p>APK for Android phones in India</p>${download('hero')}<a href="#install" class="installation-link">Installation steps ${icon('arrow')}</a></aside>
</section>
<section class="gallery-section" aria-labelledby="gallery-heading"><div class="section-heading"><div><h2 id="gallery-heading">Screenshots</h2></div><div class="gallery-controls"><button class="circle-button gallery-prev" type="button" aria-label="Previous images">${icon('back')}</button><button class="circle-button gallery-next" type="button" aria-label="Next images">${icon('arrow')}</button></div></div>
<div class="gallery-track" aria-label="Application screenshots" tabindex="0">${gallery.map((item, i) => `<figure class="gallery-card"><button class="gallery-open" data-gallery="${i}" type="button" aria-label="Enlarge ${e(item.title)}">${galleryImage(item,i)}<span class="enlarge-badge">${icon('expand')}</span></button></figure>`).join('')}</div></section>
<div class="content-grid"><div class="main-content">
<section id="about" class="about-section section-block" aria-labelledby="about-heading"><div class="section-heading"><h2 id="about-heading">About this app</h2>${icon('arrow','section-arrow')}</div><p class="about-copy">${e(config.about)}</p><div class="topic-tags"><span>Slots</span><span>Arcade</span><span>Fishing</span><span>UPI</span><span>Bank withdrawal</span><span>18+</span></div></section>
${reviewsHtml}
<section id="install" class="install-section section-block" aria-labelledby="install-heading"><span class="eyebrow">INSTALL ON ANDROID</span><h2 id="install-heading">How to install JAIHO777</h2><p class="section-intro">Four quick steps for phones in India.</p><ol class="install-steps"><li><span class="step-number">1</span><div><h3>Download the official APK</h3><p>Tap <strong>Install</strong> to save ${e(a.filename)} on your phone.</p></div></li><li><span class="step-number">2</span><div><h3>Open the file</h3><p>Open Chrome Downloads or the Files app, then tap the APK.</p></div></li><li><span class="step-number">3</span><div><h3>Allow install</h3><p>If Android asks, allow installs from this browser or source, then continue.</p></div></li><li><span class="step-number">4</span><div><h3>Open JAIHO777</h3><p>Launch the app, sign in with your mobile number, and start playing.</p></div></li></ol><div class="install-note">${icon('info')}<p>Android may show a warning for apps installed outside Play Store. That is normal for APK installs. Keep Google Play Protect on.</p></div></section>
<section id="help" class="help-section section-block" aria-labelledby="help-heading"><h2 id="help-heading">Data safety &amp; FAQ</h2><div class="faq-list"><details><summary>Is this available on Google Play? ${icon('plus')}</summary><p>JAIHO777 is distributed as an official Android APK from this download page. The Install button delivers the app file directly—no Play Store redirect.</p></details><details><summary>Which phones are supported in India? ${icon('plus')}</summary><p>Any Android ${e(a.minimumAndroid)}+ phone, including Samsung, Xiaomi, Realme, Vivo, Oppo and OnePlus. File size is ${fileSize}.</p></details><details><summary>Where is the downloaded APK saved? ${icon('plus')}</summary><p>Check Chrome Downloads or the Downloads folder in Files. Look for ${e(a.filename)}.</p></details><details><summary>How fast are withdrawals? ${icon('plus')}</summary><p>Most bank withdrawals are processed in minutes. Track every payout under My Transactions → Withdrawals.</p></details></div></section>
</div><aside class="details-column"><section id="app-details" class="app-details" aria-labelledby="details-heading"><span class="eyebrow">APP INFO</span><h2 id="details-heading">App details</h2><dl><div><dt>Version</dt><dd>${e(a.version)}</dd></div><div><dt>Updated on</dt><dd>${e(config.updatedAt)}</dd></div><div><dt>Download size</dt><dd>${fileSize}</dd></div><div><dt>Requires Android</dt><dd>${e(a.minimumAndroid)} and up</dd></div><div><dt>Downloads</dt><dd>${downloadsLabel}</dd></div><div><dt>Content rating</dt><dd>Rated for 18+</dd></div><div><dt>Interactive elements</dt><dd>Users Interact, In-Game Purchases</dd></div><div><dt>Offered by</dt><dd>${publisher ? e(publisher) : '<span class="muted">JAIHO777 Games</span>'}</dd></div></dl><details class="file-details"><summary>Developer contact &amp; file info ${icon('plus')}</summary><p class="small-label">SUPPORT</p><code>${e(config.supportHandle)}</code><p class="small-label">PACKAGE NAME</p><code>${e(a.packageName)}</code><p class="small-label">SHA-256 CHECKSUM</p><code class="checksum">${e(a.sha256)}</code><p class="checksum-note">Use the checksum to confirm the APK matches this release.</p></details></section><div class="android-card">${icon('phone')}<p>Built for<br><strong>Android in India.</strong></p><span>Direct APK · Fast install · Bank withdrawals</span></div></aside></div>
</main><footer class="site-footer"><div class="footer-inner"><div><a class="brand footer-brand" href="/">JAIHO<span class="brand-number">777</span></a><p>Official Android APK download for India.</p></div><div class="footer-links"><button class="text-button" type="button" data-privacy>Privacy</button><a href="#app-details">App details</a><span>18+ only</span></div></div><p class="footer-disclaimer">JAIHO777 Games. This page is an official APK download site and is not affiliated with Google Play. Play responsibly. Availability depends on your location and the app’s terms.</p></footer>
<div class="mobile-download" aria-label="Quick download"><div class="sticky-identity"><img src="${e(config.icon)}" width="40" height="40" alt=""><div><strong>JAIHO777</strong><span>Android · ${fileSize}</span></div></div>${download('sticky','sticky-button')}</div>
<dialog id="image-dialog" class="image-dialog" aria-labelledby="image-dialog-title"><div class="lightbox-top"><p id="image-dialog-title"></p><button class="circle-button lightbox-close" data-close-dialog type="button" aria-label="Close image preview">${icon('close')}</button></div><div class="lightbox-stage"><button class="circle-button lightbox-prev" type="button" aria-label="Previous image">${icon('back')}</button><div id="lightbox-image"></div><button class="circle-button lightbox-next" type="button" aria-label="Next image">${icon('arrow')}</button></div><p class="lightbox-count" aria-live="polite"></p></dialog>
<dialog id="privacy-dialog" class="privacy-dialog" aria-labelledby="privacy-title"><div class="privacy-heading"><h2 id="privacy-title">Your privacy</h2><button class="circle-button" data-close-dialog type="button" aria-label="Close privacy information">${icon('close')}</button></div><p>This page uses no advertising cookies or persistent visitor identifiers.</p><p>Campaign labels, such as the WhatsApp or SMS campaign name, may be held in this tab for up to ${config.attribution.ttlMinutes} minutes and carried to the download request. Do not put personal information in campaign links.</p><p>${config.analytics.enabled ? 'Anonymous campaign events are enabled. Browser privacy preferences (Do Not Track and Global Privacy Control) are respected.' : 'Analytics collection is currently disabled.'}</p><p>The hosting and file delivery providers may process ordinary connection data to serve this website and APK. This notice covers the download page, not the installed app.</p><button class="privacy-done" data-close-dialog type="button">Got it</button></dialog>
<p id="download-status" class="sr-only" role="status" aria-live="polite"></p>
</body></html>`;
}
