(() => {
  'use strict';
  const config = JSON.parse(document.getElementById('page-config').textContent);
  const params = new URLSearchParams(location.search);
  const privateMode = navigator.doNotTrack === '1' || navigator.globalPrivacyControl === true;
  const safeValue = value => typeof value === 'string' && value.length <= config.attribution.maxValueLength && !/[\u0000-\u001f@]/.test(value) && !/\d{10,}/.test(value) && !/https?:\/\//i.test(value);
  const current = {};
  for (const key of config.attribution.keys) {
    const value = params.get(key);
    if (value && safeValue(value)) current[key] = value;
  }
  let attribution = current;
  try {
    const raw = sessionStorage.getItem('jaiho777-campaign');
    if (!Object.keys(current).length && raw && !privateMode) {
      const stored = JSON.parse(raw);
      if (stored.expires > Date.now()) {
        attribution = Object.fromEntries(Object.entries(stored.values || {}).filter(([key, value]) => config.attribution.keys.includes(key) && safeValue(value)));
      } else sessionStorage.removeItem('jaiho777-campaign');
    }
    if (privateMode) sessionStorage.removeItem('jaiho777-campaign');
    else if (Object.keys(current).length) {
      sessionStorage.setItem('jaiho777-campaign', JSON.stringify({
        values: current,
        expires: Date.now() + config.attribution.ttlMinutes * 60000
      }));
    }
  } catch { /* Downloads still work without storage. */ }

  // Default SMS blast attribution when the page itself is the channel landing.
  if (!attribution.utm_source) attribution = { ...attribution, utm_source: 'sms', utm_medium: attribution.utm_medium || 'sms' };

  for (const link of document.querySelectorAll('[data-download]')) {
    const target = new URL(config.downloadUrl || link.getAttribute('href'), document.baseURI);
    for (const [key, value] of Object.entries(attribution)) target.searchParams.set(key, value);
    link.href = target.href;
    link.addEventListener('click', () => {
      const status = document.getElementById('download-status');
      if (status) status.textContent = 'APK download requested. Check your browser’s Downloads for progress.';
    });
  }

  if (config.analytics.enabled && !privateMode) {
    const payload = JSON.stringify({ event: 'page_view', attribution });
    if (navigator.sendBeacon) navigator.sendBeacon('/api/events', new Blob([payload], { type: 'application/json' }));
    else fetch('/api/events', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: payload, keepalive: true }).catch(() => {});
  }
})();
