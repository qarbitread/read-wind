const paths = {
  download: '<path d="M12 3v12m-4-4 4 4 4-4M5 16v4h14v-4"/>',
  arrow: '<path d="m9 5 7 7-7 7"/>',
  back: '<path d="m15 5-7 7 7 7"/>',
  expand: '<path d="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5"/>',
  close: '<path d="m6 6 12 12M6 18 18 6"/>',
  android: '<path d="m7 3 2 3m8-3-2 3M5 12a7 7 0 0 1 14 0v6H5v-6Zm3 6v3m8-3v3M2 12v5m20-5v5M9 10h.01M15 10h.01"/>',
  help: '<circle cx="12" cy="12" r="9"/><path d="M9.7 8.3a2.5 2.5 0 0 1 4.6 1.3c0 1.7-2.3 2.1-2.3 3.9M12 17h.01"/>',
  check: '<path d="m5 12 4 4L19 6"/>',
  info: '<circle cx="12" cy="12" r="9"/><path d="M12 11v6m0-10h.01"/>',
  plus: '<path d="M12 5v14M5 12h14"/>',
  phone: '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M10 18h4"/>'
};
export function icon(name) {
  if (!paths[name]) throw new Error(`Unknown icon: ${name}`);
  return `<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${paths[name]}</svg>`;
}
