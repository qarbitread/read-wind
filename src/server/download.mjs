export const APK_TYPE = 'application/vnd.android.package-archive';

export async function streamApk(request, release, fetchImpl) {
  const source = new URL(release.url);
  if (source.protocol !== 'https:') return { error: 503 };
  const headers = new Headers({ Accept: APK_TYPE, 'Accept-Encoding': 'identity' });
  const range = request.headers.get('Range');
  if (range) {
    if (!/^bytes=(?:\d+-\d*|-\d+)$/.test(range)) {
      return { error: 416, headers: { 'Content-Range': `bytes */${release.sizeBytes}` } };
    }
    headers.set('Range', range);
  }
  const ifRange = request.headers.get('If-Range');
  if (ifRange && ifRange.length < 200) headers.set('If-Range', ifRange);

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 25_000);
  let upstream;
  try {
    upstream = await fetchImpl(source.href, {
      method: request.method === 'HEAD' ? 'HEAD' : 'GET',
      headers, redirect: 'error', signal: controller.signal
    });
  } catch {
    return { error: 503 };
  } finally {
    // Only connection/headers time out; a slow downstream download can continue.
    clearTimeout(timeout);
  }

  if (upstream.status === 416) {
    await upstream.body?.cancel();
    return { error: 416, headers: { 'Content-Range': `bytes */${release.sizeBytes}` } };
  }
  if (![200, 206].includes(upstream.status)) {
    await upstream.body?.cancel();
    return { error: 503 };
  }
  const type = (upstream.headers.get('Content-Type') || '').split(';')[0].trim();
  if (type && ![APK_TYPE, 'application/octet-stream', 'binary/octet-stream', 'application/zip'].includes(type)) {
    await upstream.body?.cancel();
    return { error: 503 };
  }
  const length = upstream.headers.get('Content-Length');
  if (upstream.status === 200 && length && Number(length) !== release.sizeBytes) {
    await upstream.body?.cancel();
    return { error: 503 };
  }
  if (upstream.status === 206) {
    const contentRange = upstream.headers.get('Content-Range') || '';
    const match = contentRange.match(/^bytes (\d+)-(\d+)\/(\d+)$/);
    if (!match || Number(match[3]) !== release.sizeBytes || Number(match[1]) > Number(match[2]) || Number(match[2]) >= release.sizeBytes
      || (length && Number(length) !== Number(match[2]) - Number(match[1]) + 1)) {
      await upstream.body?.cancel();
      return { error: 503 };
    }
  }

  const outputHeaders = {
    'Content-Type': APK_TYPE,
    'Content-Disposition': `attachment; filename="${release.filename}"; filename*=UTF-8''${encodeURIComponent(release.filename)}`,
    'Cache-Control': 'private, no-store',
    'Accept-Ranges': 'bytes',
    'X-Robots-Tag': 'noindex, nofollow',
    'X-Download-SHA256': release.sha256
  };
  for (const key of ['Content-Length', 'Content-Range', 'ETag', 'Last-Modified']) {
    const value = upstream.headers.get(key);
    if (value) outputHeaders[key] = value;
  }
  return { status: upstream.status, body: request.method === 'HEAD' ? null : upstream.body, headers: outputHeaders };
}
