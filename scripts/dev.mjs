import http from 'node:http';
import {Readable} from 'node:stream';
import {stat,readFile} from 'node:fs/promises';
import {pathToFileURL} from 'node:url';
import {execFileSync} from 'node:child_process';
import path from 'node:path';

const root=path.resolve(import.meta.dirname,'..');
execFileSync(process.execPath,[path.join(root,'scripts/build.mjs')],{cwd:root,stdio:'inherit'});
const entry=path.join(root,'dist/server/index.js');
const escapeAttribute=value=>value.replaceAll('&','&amp;').replaceAll('"','&quot;').replaceAll('<','&lt;').replaceAll('>','&gt;');
const server=http.createServer(async(request,response)=>{
  try{
    if(request.url.startsWith('/__qa/mobile')){
      const query=new URL(request.url,'http://localhost').searchParams;
      const requested=Number(query.get('width'));
      const width=[320,360,390,430,768].includes(requested)?requested:390;
      const html=await readFile(path.join(root,'dist/public/index.html'),'utf8');
      const host=String(request.headers.host||'localhost').replace(/[^a-zA-Z0-9.:\-]/g,'');
      const page=html.replace('<head>',`<head><base href="http://${host}/">`);
      response.writeHead(200,{'Content-Type':'text/html; charset=utf-8','Cache-Control':'no-store'});
      response.end(`<!doctype html><html lang="en"><meta charset="utf-8"><title>JAIHO777 mobile preview</title><style>body{margin:0;background:#eef2ef;display:flex;justify-content:center;padding:24px;min-height:100vh;box-sizing:border-box}iframe{width:${width}px;height:844px;max-width:100%;border:1px solid #cdd8d0;border-radius:15px;background:#fff;box-shadow:0 8px 28px #163c2212}</style><iframe title="JAIHO777 mobile preview" srcdoc="${escapeAttribute(page)}"></iframe></html>`);
      return;
    }
    const stamp=(await stat(entry)).mtimeMs;
    const worker=(await import(pathToFileURL(entry).href+`?v=${stamp}`)).default;
    const local=request.headers.host?.startsWith('localhost')||request.headers.host?.startsWith('127.0.0.1');
    const url=`${local?'http':'https'}://${request.headers.host}${request.url}`;
    const init={method:request.method,headers:request.headers};
    if(!['GET','HEAD'].includes(request.method)){init.body=Readable.toWeb(request);init.duplex='half';}
    const result=await worker.fetch(new Request(url,init),{});
    const headers=new Headers(result.headers);headers.set('Cache-Control','no-store');
    response.writeHead(result.status,Object.fromEntries(headers));
    if(result.body)Readable.fromWeb(result.body).pipe(response);else response.end();
  }catch(error){console.error(error.message);response.writeHead(500,{'Content-Type':'text/plain'});response.end('Preview error');}
});
const portIndex=process.argv.indexOf('--port');
const port=Number(portIndex>=0?process.argv[portIndex+1]:process.env.PORT||3000);
server.listen(port,'0.0.0.0',()=>console.log(`JAIHO777 preview listening on ${port}`));
