import assert from 'node:assert/strict';
import { readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

// Live acceptance check: hash the stream without saving or executing the APK.
const root = path.resolve(import.meta.dirname, '..');
const release = JSON.parse(await readFile(path.join(root, 'config/release.json'), 'utf8'));
const report = JSON.parse(await readFile(path.join(root, 'dist/reports/build-report.json'), 'utf8'));
const worker = (await import(pathToFileURL(path.join(root, 'dist/server/index.js')).href)).default;
const url = report.origin + '/download?utm_source=qa&utm_campaign=release-check';
const head = await worker.fetch(new Request(url, { method: 'HEAD' }));
assert.equal(head.status, 200);
assert.equal(Number(head.headers.get('Content-Length')), release.sizeBytes);
assert.equal(head.headers.get('Content-Type'), 'application/vnd.android.package-archive');
assert.ok(head.headers.get('Content-Disposition').startsWith('attachment;'));
assert.equal(head.headers.get('Location'), null);
const range = await worker.fetch(new Request(url, { headers: { Range: 'bytes=0-1023' } }));
assert.equal(range.status, 206);
assert.equal(range.headers.get('Content-Range'), `bytes 0-1023/${release.sizeBytes}`);
assert.equal((await range.arrayBuffer()).byteLength, 1024);
const response = await worker.fetch(new Request(url));
assert.equal(response.status, 200);
const hash = createHash('sha256');
const reader = response.body.getReader();
let bytes = 0;
while (true) {
  const chunk = await reader.read();
  if (chunk.done) break;
  bytes += chunk.value.length;
  hash.update(chunk.value);
}
const checksum = hash.digest('hex');
assert.equal(bytes, release.sizeBytes);
assert.equal(checksum, release.sha256);
const result = { checkedAt: new Date().toISOString(), version: release.version, status: response.status,
  headStatus: head.status, rangeStatus: range.status, sizeBytes: bytes, sha256: checksum,
  contentType: response.headers.get('Content-Type'), attachment: true, redirect: false };
await writeFile(path.join(root, 'dist/reports/download-check.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify(result, null, 2));
