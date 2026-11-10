export function collectAttribution(input, rules) {
  const read = key => input instanceof URLSearchParams ? input.get(key) : input?.[key];
  const result = {};
  for (const key of rules.keys) {
    const value = read(key);
    if (typeof value === 'string' && value.length > 0 && value.length <= rules.maxValueLength
      && !/[\u0000-\u001f@]/.test(value) && !/\d{10,}/.test(value) && !/https?:\/\//i.test(value)) {
      result[key] = value;
    }
  }
  return result;
}

export function privacyOptOut(request) {
  return request.headers.get('DNT') === '1' || request.headers.get('Sec-GPC') === '1';
}

export function recordEvent(request, env, site, name, attribution) {
  if (!site.analytics.enabled || privacyOptOut(request) || !env?.ANALYTICS?.writeDataPoint) return;
  try {
    env.ANALYTICS.writeDataPoint({
      indexes: [name],
      blobs: [attribution.utm_source || attribution.source || 'direct', attribution.utm_medium || '',
        attribution.utm_campaign || '', attribution.utm_content || ''],
      doubles: [1]
    });
  } catch {
    // Optional metrics never block the page or an APK response.
  }
}

export async function readSmallJson(request, maximum = 2048) {
  if (Number(request.headers.get('Content-Length') || 0) > maximum) return { status: 413 };
  const reader = request.body?.getReader();
  if (!reader) return { status: 400 };
  const chunks = [];
  let length = 0;
  try {
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      length += value.length;
      if (length > maximum) { await reader.cancel(); return { status: 413 }; }
      chunks.push(value);
    }
    const bytes = new Uint8Array(length);
    let offset = 0;
    for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
    return { value: JSON.parse(new TextDecoder().decode(bytes)) };
  } catch {
    return { status: 400 };
  }
}
