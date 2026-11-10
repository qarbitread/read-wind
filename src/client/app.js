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
        attribution = Object.fromEntries(Object.entries(stored.values || {}).filter(([key,value]) => config.attribution.keys.includes(key) && safeValue(value)));
      } else sessionStorage.removeItem('jaiho777-campaign');
    }
    if (privateMode) sessionStorage.removeItem('jaiho777-campaign');
    else if (Object.keys(current).length) sessionStorage.setItem('jaiho777-campaign', JSON.stringify({values:current,expires:Date.now() + config.attribution.ttlMinutes * 60000}));
  } catch { /* Downloads work even when browser storage is disabled. */ }
  for (const link of document.querySelectorAll('[data-download]')) {
    const target = new URL('/download', document.baseURI);
    for (const [key,value] of Object.entries(attribution)) target.searchParams.set(key,value);
    link.href = target.pathname + target.search;
    link.addEventListener('click', () => {
      document.getElementById('download-status').textContent = 'APK download requested. Check your browser’s Downloads for progress.';
    });
  }
  if (config.analytics.enabled && !privateMode) {
    const payload = JSON.stringify({event:'page_view',attribution});
    if (navigator.sendBeacon) navigator.sendBeacon('/api/events', new Blob([payload], {type:'application/json'}));
    else fetch('/api/events', {method:'POST',headers:{'Content-Type':'application/json'},body:payload,keepalive:true}).catch(()=>{});
  }
  const track = document.querySelector('.gallery-track');
  const prev = document.querySelector('.gallery-prev');
  const next = document.querySelector('.gallery-next');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const scroll = direction => track.scrollBy({left:direction * (track.querySelector('.gallery-card').offsetWidth + (parseFloat(getComputedStyle(track).columnGap) || 0)), behavior:reduced?'instant':'smooth'});
  prev.addEventListener('click',()=>scroll(-1));
  next.addEventListener('click',()=>scroll(1));
  function updateArrows() {
    const isScrollable = track.scrollWidth > track.clientWidth + 2;
    prev.disabled = !isScrollable || track.scrollLeft < 2;
    next.disabled = !isScrollable || track.scrollLeft + track.clientWidth >= track.scrollWidth - 2;
  }
  track.addEventListener('scroll',updateArrows,{passive:true});
  window.addEventListener('resize',updateArrows,{passive:true});
  updateArrows();
  track.addEventListener('keydown', event => {
    if (event.target !== track) return;
    if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') { event.preventDefault(); scroll(event.key === 'ArrowRight'?1:-1); }
  });
  const imageDialog = document.getElementById('image-dialog');
  const privacyDialog = document.getElementById('privacy-dialog');
  let selected = 0, returnFocus;
  function showImage(index) {
    selected = (index + config.gallery.length) % config.gallery.length;
    const item = config.gallery[selected];
    document.getElementById('image-dialog-title').textContent = item.title;
    document.getElementById('lightbox-image').innerHTML = item.html;
    document.querySelector('.lightbox-count').textContent = `${selected+1} / ${config.gallery.length}`;
  }
  function open(dialog, trigger) { returnFocus=trigger; dialog.showModal(); document.body.classList.add('modal-open'); }
  document.querySelectorAll('[data-gallery]').forEach(button=>button.addEventListener('click',()=>{showImage(Number(button.dataset.gallery));open(imageDialog,button);}));
  document.querySelector('.lightbox-prev').addEventListener('click',()=>showImage(selected-1));
  document.querySelector('.lightbox-next').addEventListener('click',()=>showImage(selected+1));
  imageDialog.addEventListener('keydown',event=>{
    if(event.key==='ArrowRight'){event.preventDefault();showImage(selected+1);}
    if(event.key==='ArrowLeft'){event.preventDefault();showImage(selected-1);}
  });
  document.querySelector('[data-privacy]').addEventListener('click',event=>open(privacyDialog,event.currentTarget));
  for(const dialog of [imageDialog,privacyDialog]){
    dialog.querySelectorAll('[data-close-dialog]').forEach(button=>button.addEventListener('click',()=>dialog.close()));
    dialog.addEventListener('click',event=>{
      if(event.target!==dialog) return;
      const r=dialog.getBoundingClientRect();
      if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom) dialog.close();
    });
    dialog.addEventListener('close',()=>{document.body.classList.remove('modal-open');returnFocus?.focus({preventScroll:true});});
  }
})();
