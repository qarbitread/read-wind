import { readFile, writeFile, readdir, mkdir, cp, rm } from 'node:fs/promises';
import { deflateRawSync } from 'node:zlib';
import { createHash } from 'node:crypto';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const argument = process.argv.slice(2).find(value => value.startsWith('--out='));
const output = path.resolve(argument ? argument.slice(6) : path.join(root, 'output'));
if (output === root || output === path.parse(output).root) throw new Error('Choose an output subdirectory, not the project or filesystem root.');
await mkdir(output, { recursive: true });
const report = JSON.parse(await readFile(path.join(root, 'dist/reports/build-report.json'), 'utf8'));

async function collect(directory, prefix = '') {
  const files = [];
  for (const item of await readdir(directory, { withFileTypes: true })) {
    if (item.name === '__pycache__' || item.name.endsWith('.pyc')) continue;
    const filename = path.join(directory, item.name);
    const relative = path.posix.join(prefix, item.name);
    if (item.isDirectory()) files.push(...await collect(filename, relative));
    else if (item.isFile()) files.push({ name: relative, bytes: await readFile(filename) });
  }
  return files.sort((a, b) => a.name.localeCompare(b.name));
}

// Small ZIP writer using only Node's standard library: no packaging dependency at runtime.
const crcTable = new Uint32Array(256).map((_, index) => {
  let value = index;
  for (let bit = 0; bit < 8; bit++) value = value & 1 ? 0xedb88320 ^ value >>> 1 : value >>> 1;
  return value >>> 0;
});
function crc32(bytes) {
  let value = 0xffffffff;
  for (const byte of bytes) value = crcTable[(value ^ byte) & 255] ^ value >>> 8;
  return (value ^ 0xffffffff) >>> 0;
}
function zip(files) {
  const local = [], central = [];
  let offset = 0;
  for (const { name, bytes } of files) {
    const filename = Buffer.from(name, 'utf8');
    const compressed = deflateRawSync(bytes, { level: 9 });
    const checksum = crc32(bytes);
    const header = Buffer.alloc(30);
    header.writeUInt32LE(0x04034b50, 0);
    header.writeUInt16LE(20, 4);
    header.writeUInt16LE(0x800, 6);
    header.writeUInt16LE(8, 8);
    header.writeUInt16LE(((2026 - 1980) << 9) | (11 << 5) | 9, 12);
    header.writeUInt32LE(checksum, 14);
    header.writeUInt32LE(compressed.length, 18);
    header.writeUInt32LE(bytes.length, 22);
    header.writeUInt16LE(filename.length, 26);
    const directory = Buffer.alloc(46);
    directory.writeUInt32LE(0x02014b50, 0);
    directory.writeUInt16LE(20, 4);
    header.copy(directory, 6, 4, 30);
    directory.writeUInt32LE(offset, 42);
    local.push(header, filename, compressed);
    central.push(directory, filename);
    offset += header.length + filename.length + compressed.length;
  }
  const directory = Buffer.concat(central);
  const ending = Buffer.alloc(22);
  ending.writeUInt32LE(0x06054b50, 0);
  ending.writeUInt16LE(files.length, 8);
  ending.writeUInt16LE(files.length, 10);
  ending.writeUInt32LE(directory.length, 12);
  ending.writeUInt32LE(offset, 16);
  return Buffer.concat([...local, directory, ending]);
}

const html = await collect(path.join(root, 'dist/readable'), 'html');
const exportedAssets = await collect(path.join(root, 'dist/public/assets'), 'html/assets');
const common = [
  ...await collect(path.join(root, 'docs'), 'docs'),
  { name: 'README.md', bytes: await readFile(path.join(root, 'README.md')) },
  { name: 'FONT-LICENSE.txt', bytes: await readFile(path.join(root, 'FONT-LICENSE.txt')) },
  ...html, ...exportedAssets,
  { name: 'html/robots.txt', bytes: await readFile(path.join(root, 'dist/public/robots.txt')) },
  { name: 'html/sitemap.xml', bytes: await readFile(path.join(root, 'dist/public/sitemap.xml')) },
  { name: 'html/favicon.ico', bytes: await readFile(path.join(root, 'dist/public/favicon.ico')) }
];
const deployment = [
  ...await collect(path.join(root, 'dist/server'), 'server'),
  ...await collect(path.join(root, 'dist/public'), 'public'),
  ...await collect(path.join(root, 'dist/reports'), 'reports'),
  ...common,
  { name: 'wrangler.toml', bytes: Buffer.from('name = "jaiho777-apk-download"\nmain = "server/index.js"\ncompatibility_date = "2026-11-09"\nworkers_dev = true\n') }
];
const source = [...common];
for (const directory of ['assets', 'config', 'public', 'scripts', 'src', 'tests']) source.push(...await collect(path.join(root, directory), directory));
for (const filename of ['package.json', 'package-lock.json', 'wrangler.toml', '.gitignore']) source.push({ name: filename, bytes: await readFile(path.join(root, filename)) });
const manifest = { origin: report.origin, version: report.version, files: {} };
for (const [filename, entries] of [['JAIHO777-deploy.zip', deployment], ['JAIHO777-source.zip', source]]) {
  const bytes = zip(entries);
  await writeFile(path.join(output, filename), bytes);
  manifest.files[filename] = { bytes: bytes.length, sha256: createHash('sha256').update(bytes).digest('hex'), entries: entries.length };
}
const readable = path.join(output, 'JAIHO777-html');
await rm(readable, { recursive: true, force: true });
await cp(path.join(root, 'dist/readable'), readable, { recursive: true });
await cp(path.join(root, 'dist/public/assets'), path.join(readable, 'assets'), { recursive: true });
for (const filename of ['robots.txt', 'sitemap.xml', 'favicon.ico']) await cp(path.join(root, 'dist/public', filename), path.join(readable, filename));
await writeFile(path.join(output, 'checksums.json'), JSON.stringify(manifest, null, 2) + '\n');
console.log(JSON.stringify(manifest, null, 2));
