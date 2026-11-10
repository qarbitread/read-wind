# JAIHO777 — website presentasi lengkap

Tampilan mengikuti ide listing unduhan Android yang nyata: header Play Store tanpa label DEMO, rating 4.8, unduhan 5M+, badge Verified App, tiga ulasan dengan foto profil, serta enam screenshot aplikasi dalam urutan yang disetujui. Pengujian membandingkan fingerprint body dan CSS untuk mencegah perubahan tampilan tidak sengaja.

Halaman dikirim sebagai HTML langsung. Tidak ada React hydration, script iklan, library animasi, font eksternal, atau dependency runtime di browser. Tombol download merupakan tautan ke endpoint server dan bekerja tanpa JavaScript. JavaScript kecil hanya menangani galeri, dialog dan atribusi kampanye.

## Menjalankan source

Gunakan Node.js 22 atau lebih baru. Dari folder source yang diekstrak, jalankan di Terminal atau PowerShell:

```bash
npm ci
npm run check
npm run dev
```

Buka `http://localhost:3000`. Setelah mengubah source, jalankan build lalu refresh halaman. Server dev bukan server produksi.

| Perintah | Fungsi |
| --- | --- |
| `npm run build` | Membuat HTML, aset minifikasi, robots, sitemap dan bundle server |
| `npm test` | Menguji download, resume, perlindungan source, atribusi, privasi dan kesamaan presentasi |
| `npm run verify` | Memeriksa metadata, URL aset, batas ukuran dan endpoint hasil build |
| `npm run check` | Build + test + verify |
| `node scripts/verify-download.mjs` | Memeriksa file APK nyata lewat handler server dan SHA-256; transfer sekitar 47.5 MB |
| `npm run package` | Membuat ZIP deployment dan ZIP source di `output/` |

## Susunan folder

| Lokasi | Isi |
| --- | --- |
| `config/site.json` | Domain, judul, description, logo, screenshot, materi demo dan kampanye |
| `config/release.json` | URL asal APK dan metadata file; tidak dilayani sebagai file publik |
| `src/presentation.mjs` | Markup dan isi tampilan presentasi yang disetujui |
| `src/render.mjs` | Penyatuan halaman, metadata, JSON-LD, robots dan sitemap |
| `src/templates/` | Kerangka HTML utama, halaman privasi dan error |
| `src/styles/site.css` | CSS presentasi asli; gaya halaman dokumen terpisah dan dibatasi scope |
| `src/client/app.js` | Carousel, preview fullscreen, dialog privasi dan kampanye |
| `src/server/` | Router, header keamanan, streaming APK dan analytics opsional |
| `public/assets/brand/` | Logo, favicon dan preview WhatsApp |
| `public/assets/screenshots/` | Screenshot penuh dan thumbnail |
| `public/assets/presentation/` | Ikon header dan foto profil contoh dari presentasi sebelumnya |
| `public/assets/fonts/` | Roboto lokal dan lisensi |
| `assets/source/` | Logo dan preview sosial sumber |
| `scripts/` | Build, formatter HTML, inspector APK, verifikasi dan pengemasan |
| `tests/fixtures/` | Baseline fingerprint presentasi yang disetujui |
| `docs/` | Panduan deployment, SEO, penggantian konten dan perlindungan kode |
| `dist/public/` | HTML minifikasi dan aset browser berhash |
| `dist/readable/` | HTML lengkap dengan indentasi |
| `dist/server/index.js` | Worker produksi, hanya dijalankan di server |
| `dist/reports/` | Ukuran build, manifest aset dan hasil cek download jika dijalankan |
| `output/` | Hasil ZIP; tidak untuk diletakkan di root publik situs |

Edit source, bukan `dist/` atau `output/`, karena kedua folder itu dibuat ulang saat build/package.

## Isi paket

`JAIHO777-deploy.zip` berisi Worker yang siap diunggah, folder `public/`, salinan HTML lengkap di `html/`, konfigurasi Wrangler dan panduan. Worker membawa HTML/aset yang dilayani tanpa database atau filesystem runtime.

`JAIHO777-source.zip` berisi kode, template, konfigurasi, aset, pengujian, lockfile, panduan dan salinan HTML lengkap di `html/`. Repository Git, kredensial, dependency terpasang, source map dan APK 47.5 MB tidak dimasukkan.

Mengunggah **hanya** index.html ke hosting statis tidak menyediakan `/download`. Gunakan bundle server agar tombol mengembalikan APK langsung dengan MIME dan attachment header yang benar.

## APK yang digunakan

Metadata dibaca dari file tanpa menjalankan aplikasinya. URL asal yang disetujui pemilik disimpan dalam `config/release.json`.

| Informasi | Nilai |
| --- | --- |
| Versi | 1.1.1 / versionCode 111 |
| Ukuran tepat | 47,516,594 byte / 47.5 MB desimal |
| Android minimum | 5.0 / API 21 |
| Package | `com.jaiho.sss.in` |
| File unduhan | `JAIHO777-1.1.1.apk` |
| SHA-256 | `98a17333248a699ecf1ecb1e78f590216f5f29ce5f55d067c557084f36f52076` |

Identitas publisher terverifikasi belum diberikan; teks `Not provided` pada presentasi sebelumnya tetap sama. Versi, ukuran dan checksum adalah metadata file, bukan sertifikasi keamanan.

## Mode listing aktif

`demoPresentation.enabled` tetap `true` agar rating, badge, dan ulasan tetap tampil sebagai bagian listing. Label DEMO dan disclosure contoh sudah dihapus. Tidak ada review/rating di structured data. Metadata memakai `index,follow` dan robots membatasi crawling endpoint unduhan/API.

## Kinerja dan batas pengujian

HTML/CSS/JS diminifikasi tanpa source maps. Aset memakai nama berhash dan ETag. Font di-host lokal. Carousel memakai thumbnail; gambar penuh dimuat ketika dibuka. Dimensi gambar sudah ditetapkan, swipe dan keyboard tetap tersedia, dan sticky download tetap mengikuti desain sebelumnya. APK dialirkan oleh server, tanpa buffer seluruh 47.5 MB di memori.

Ukuran aktual tersedia di `dist/reports/build-report.json`. Skor Lighthouse 90+ belum diukur dan tidak dijanjikan. Setelah domain publik dipasang, uji Chrome Android, WhatsApp dan SMS di perangkat nyata; browser/perangkat mengendalikan dialog file serta peringatan keamanan Android.

## Panduan lengkap

- [Deployment dan pemeriksaan setelah upload](docs/DEPLOYMENT.md)
- [Metadata, robots, sitemap dan kampanye](docs/SEO-AND-TRACKING.md)
- [Mengganti logo, screenshot, APK dan konten](docs/EDITING.md)
- [Perlindungan kode dan batas teknis](docs/CODE-PROTECTION.md)

## Asal aset

Logo asli berasal dari aset pemilik yang sebelumnya digunakan: `https://www.prosafeimg.com/uploads/20260731/6a6c6e378c7f6.png`. Enam screenshot disediakan pemilik dan dipertahankan utuh. Halaman menyatakan dirinya independen dan tidak berafiliasi dengan Google Play. Roboto disertakan dengan lisensi Apache 2.0, lihat `FONT-LICENSE.txt`.
