# Deployment JAIHO777

## Siapkan domain

Paket ini mempertahankan presentasi yang disetujui. Site review native tetap private; domain publik untuk penerima WhatsApp/SMS belum ditentukan.

Dari folder source, ubah `origin` di `config/site.json` menjadi origin HTTPS milik Anda, misalnya `https://download.example.com`. Jangan masukkan path, query atau fragment. Kemudian:

```bash
npm ci
npm run check
```

Alternatif untuk satu build:

```bash
npm run build -- --origin=https://download.example.com
npm test
npm run verify
```

Override tidak mengubah konfigurasi sumber. Build berikutnya tanpa override kembali mengikuti origin konfigurasi. Canonical, Open Graph URL, gambar sosial, JSON-LD, robots dan sitemap diperbarui bersama oleh build; jangan mengedit sitemap saja.

## Cloudflare Worker

Gunakan Node.js 22+ dan akun Cloudflare. Dari folder source yang sudah dibangun:

```bash
npx wrangler login
npx wrangler deploy
```

Konfigurasi source menunjuk ke `dist/server/index.js`. Jika memakai ZIP deployment, ekstrak dan jalankan perintah yang sama dari folder `wrangler.toml`; konfigurasi ZIP menunjuk ke `server/index.js`. Paket deployment tidak membutuhkan perintah build atau npm install karena modul sudah dibundel.

Worker memakai satu modul ES tanpa database, Pages Functions atau binding static assets. Folder `public/` adalah export untuk inspeksi; aset yang disajikan sudah ada dalam allowlist modul server.

## Custom domain dan HTTPS

Di Cloudflare, buka Worker → Settings → Domains & Routes → Add → Custom Domain. Pilih domain yang Anda kendalikan pada zone akun tersebut, lalu pastikan origin source sama dengan domain yang terpasang.

Untuk pengelolaan melalui Wrangler, contoh konfigurasi:

```toml
routes = [
  { pattern = "download.example.com", custom_domain = true }
]
```

Ganti domain contoh. Setelah custom domain berhasil, `workers_dev = false` dapat dipakai bila tidak menginginkan URL alternatif workers.dev. Tidak ada domain yang dibeli atau didaftarkan oleh paket ini.

## Periksa hasil deployment

Linux/macOS:

```bash
curl -I 'https://download.example.com/'
curl -I 'https://download.example.com/download?utm_source=whatsapp&utm_campaign=check'
curl -I -H 'Range: bytes=0-1023' 'https://download.example.com/download'
curl --fail 'https://download.example.com/download' -o jaiho777-check.apk
sha256sum jaiho777-check.apk
```

PowerShell Windows:

```powershell
curl.exe -I "https://download.example.com/"
curl.exe -I "https://download.example.com/download?utm_source=whatsapp&utm_campaign=check"
curl.exe -I -H "Range: bytes=0-1023" "https://download.example.com/download"
curl.exe --fail "https://download.example.com/download" -o jaiho777-check.apk
Get-FileHash .\jaiho777-check.apk -Algorithm SHA256
```

Harapkan 200 untuk file penuh, `Content-Type: application/vnd.android.package-archive`, `Content-Disposition: attachment`, panjang 47,516,594 byte dan SHA-256 sesuai release.json. Range harus menghasilkan 206/Content-Range. Header attachment tidak meniadakan dialog unduhan atau peringatan Android.

Periksa `/robots.txt`, `/sitemap.xml`, `/privacy/`, preview sosial, dan URL acak yang harus 404. `/config/release.json`, `/src/`, `/.git/config` dan `/package.json` harus 404. Query `?url=...` tidak boleh mengganti source APK yang ditentukan server.

## Uji kampanye dan pemeliharaan

Uji tautan melalui WhatsApp/SMS pada perangkat sendiri: preview, download, nama file, swipe enam screenshot, fullscreen dan sticky CTA. Jika in-app browser membatasi file, petunjuk di halaman menyarankan membuka halaman yang sama di Chrome.

Untuk update, simpan arsip source, edit konfigurasi/aset, jalankan check dan deploy kembali. Aset berhash mencegah CSS/JS lama tertukar. Rollback dilakukan dengan bundle server sebelumnya; sumber APK harus masih tersedia dan sesuai checksum.

Hosting lain membutuhkan adapter server untuk API Fetch dan streaming. Server dev bukan reverse proxy produksi. Jangan unggah seluruh source sebagai folder publik dan jangan hanya mengunggah HTML ke static hosting lalu menganggap endpoint download tersedia.

## Rujukan

- [Konfigurasi Wrangler](https://developers.cloudflare.com/workers/wrangler/configuration/)
- [Custom Domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/)
