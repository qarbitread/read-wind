import {readFile,writeFile,readdir,mkdir,rm,copyFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {gzipSync,brotliCompressSync} from 'node:zlib';
import path from 'node:path';
import {build,transform} from 'esbuild';
import {minify} from 'html-minifier-terser';
import {renderPages} from '../src/render.mjs';
import {readableHtml} from './format-html.mjs';

const root=path.resolve(import.meta.dirname,'..');
const output=path.join(root,'dist');
const readJson=async file=>JSON.parse(await readFile(path.join(root,file),'utf8'));
const site=await readJson('config/site.json');
const release=await readJson('config/release.json');
const args=process.argv.slice(2);
const originArg=args.find(value=>value.startsWith('--origin='));
if(args.some(value=>!value.startsWith('--origin=')))throw new Error('Supported build option: --origin=https://your-domain.example');
if(originArg)site.origin=originArg.slice('--origin='.length);
const origin=new URL(site.origin);
if(origin.protocol!=='https:'||origin.username||origin.password||origin.pathname!=='/'||origin.search||origin.hash)throw new Error('origin must be an HTTPS origin without a path, credentials, query, or fragment');
site.origin=origin.origin;
const upstream=new URL(release.url);
if(upstream.protocol!=='https:'||upstream.username||upstream.password)throw new Error('The server-side APK source must be HTTPS');
if(!/^[\w.-]+\.apk$/.test(release.filename))throw new Error('APK filename must be a safe .apk filename');
if(!Number.isSafeInteger(release.sizeBytes)||release.sizeBytes<1||!/^[a-f0-9]{64}$/.test(release.sha256))throw new Error('Inspect the APK before building: real file size and SHA-256 are required');
if(!release.version||!release.packageName||!release.minimumAndroid)throw new Error('Release metadata is incomplete');
if(!/^\d{4}-\d{2}-\d{2}$/.test(site.updatedAt))throw new Error('Use an ISO date in site.updatedAt');
if(site.publisherVerified&&!site.publisher)throw new Error('A verified publisher requires a supplied name');
if(!site.screenshots.length)throw new Error('Owner-supplied app screenshots are required');

await rm(output,{recursive:true,force:true});
for(const dir of ['public','public/privacy','public/sms','server','readable/privacy','readable/sms','reports','.openai'])await mkdir(path.join(output,dir),{recursive:true});
const types={'.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.webp':'image/webp','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.ico':'image/x-icon','.woff2':'font/woff2','.txt':'text/plain; charset=utf-8'};
const files={};
const assets={};
const assetSizes={};
const digest=bytes=>createHash('sha256').update(bytes).digest('hex');
async function addAsset(original,bytes){
  const extension=path.extname(original);
  if(!types[extension])throw new Error(`Unsupported public asset type: ${original}`);
  const hash=digest(bytes);
  const stem=original.slice(0,-extension.length);
  const uri=`${stem}.${hash.slice(0,12)}${extension}`;
  const target=path.join(output,'public',uri.slice(1));
  await mkdir(path.dirname(target),{recursive:true});
  await writeFile(target,bytes);
  files[original]=uri;
  assets[uri]={base64:bytes.toString('base64'),size:bytes.byteLength,type:types[extension],etag:`"${hash.slice(0,24)}"`,immutable:true};
  assetSizes[original]=bytes.byteLength;
  return uri;
}
async function collect(directory){
  for(const entry of await readdir(directory,{withFileTypes:true})){
    const file=path.join(directory,entry.name);
    if(entry.isDirectory())await collect(file);
    else await addAsset('/'+path.relative(path.join(root,'public'),file).split(path.sep).join('/'),await readFile(file));
  }
}
await collect(path.join(root,'public/assets'));
for(const screenshot of site.screenshots){
  for(const key of ['src','thumbnailSrc'])if(!files[screenshot[key]])throw new Error(`Screenshot asset missing: ${screenshot[key]}`);
  if(!screenshot.title||!screenshot.alt||!screenshot.width||!screenshot.height)throw new Error('Every screenshot requires a title, alt text, width, and height');
}
for(const key of ['icon','iconSmall','iconLarge','favicon','faviconPng','appleIcon','socialImage'])if(!files[site[key]])throw new Error(`Brand asset missing: ${site[key]}`);
let css=await readFile(path.join(root,'src/styles/site.css'),'utf8');
for(const [original,uri]of Object.entries(files))css=css.split(original).join(uri);
const cssResult=await transform(css,{loader:'css',minify:true,legalComments:'none',target:['chrome80','safari13']});
files.styles=await addAsset('/assets/css/site.min.css',Buffer.from(cssResult.code));
let smsCss=await readFile(path.join(root,'src/styles/sms.css'),'utf8');
for(const [original,uri]of Object.entries(files))smsCss=smsCss.split(original).join(uri);
const smsCssResult=await transform(smsCss,{loader:'css',minify:true,legalComments:'none',target:['chrome80','safari13']});
files.smsStyles=await addAsset('/assets/css/sms.min.css',Buffer.from(smsCssResult.code));
const client=await readFile(path.join(root,'src/client/app.js'),'utf8');
const jsResult=await transform(client,{loader:'js',minify:true,legalComments:'none',target:'es2018',charset:'utf8'});
files.script=await addAsset('/assets/js/app.min.js',Buffer.from(jsResult.code));
const smsClient=await readFile(path.join(root,'src/client/sms.js'),'utf8');
const smsJsResult=await transform(smsClient,{loader:'js',minify:true,legalComments:'none',target:'es2018',charset:'utf8'});
files.smsScript=await addAsset('/assets/js/sms.min.js',Buffer.from(smsJsResult.code));
const rendered=renderPages(site,release,files);
const pages={...rendered};
for(const key of ['index','sms','privacy','notFound','downloadError']){
  pages[key]=await minify(rendered[key],{collapseWhitespace:true,conservativeCollapse:true,removeComments:true,removeAttributeQuotes:false,collapseBooleanAttributes:true,minifyCSS:false,minifyJS:false});
  if(pages[key].includes('{{'))throw new Error(`Unresolved template data in ${key}`);
}
if(!pages.index.includes(`href="${release.url}"`))throw new Error('Install buttons must use the direct release APK URL');
if(!pages.sms.includes(`href="${release.url}"`))throw new Error('SMS Install button must use the direct release APK URL');
const publicPages={'index.html':pages.index,'sms/index.html':pages.sms,'privacy/index.html':pages.privacy,'404.html':pages.notFound,'robots.txt':pages.robots,'sitemap.xml':pages.sitemap};
for(const [relative,body]of Object.entries(publicPages))await writeFile(path.join(output,'public',relative),body);
await writeFile(path.join(output,'readable/index.html'),readableHtml(rendered.index));
await writeFile(path.join(output,'readable/sms/index.html'),readableHtml(rendered.sms));
await writeFile(path.join(output,'readable/privacy/index.html'),readableHtml(rendered.privacy));
await copyFile(path.join(output,'public',files[site.favicon].slice(1)),path.join(output,'public/favicon.ico'));
assets['/favicon.ico']={...assets[files[site.favicon]],immutable:false};

const code=`import {createWorker} from './src/server/index.mjs';\nexport default createWorker(${JSON.stringify({site,release,assets,pages})});`;
await build({stdin:{contents:code,resolveDir:root,sourcefile:'production-entry.mjs',loader:'js'},bundle:true,format:'esm',platform:'browser',target:'es2022',minify:true,sourcemap:false,legalComments:'none',charset:'utf8',outfile:path.join(output,'server/index.js'),logLevel:'silent'});
try{await copyFile(path.join(root,'.openai/hosting.json'),path.join(output,'.openai/hosting.json'));}catch(error){if(error.code!=='ENOENT')throw error;}
const indexBytes=Buffer.from(pages.index);
const report={
  origin:site.origin,updatedAt:site.updatedAt,version:release.version,
  html:{bytes:indexBytes.length,gzipBytes:gzipSync(indexBytes).length,brotliBytes:brotliCompressSync(indexBytes).length},
  css:{bytes:Buffer.byteLength(cssResult.code),gzipBytes:gzipSync(cssResult.code).length},
  javascript:{bytes:Buffer.byteLength(jsResult.code),gzipBytes:gzipSync(jsResult.code).length},
  thumbnailBytes:site.screenshots.reduce((sum,image)=>sum+(assetSizes[image.thumbnailSrc]||0),0),
  fullScreenshotCount:site.screenshots.length,publicAssetCount:Object.keys(assets).length,
  workerBytes:(await readFile(path.join(output,'server/index.js'))).length,
  sourceMaps:false,thirdPartyBrowserScripts:0,assetManifest:files
};
await writeFile(path.join(output,'reports/build-report.json'),JSON.stringify(report,null,2)+'\n');
console.log(`Production build: HTML ${report.html.bytes} B (${report.html.gzipBytes} B gzip), CSS ${report.css.bytes} B, JS ${report.javascript.bytes} B.`);
console.log(`Screenshots: ${report.fullScreenshotCount}, thumbnails ${report.thumbnailBytes} B total. No source maps or third-party browser scripts.`);
