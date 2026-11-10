# Penggantian konten dan aset

Tampilan listing unduhan mengikuti layout yang disetujui tanpa label DEMO. Panduan ini untuk pemeliharaan berikutnya; build tidak mengganti copy atau susunan screenshot otomatis.

| Perubahan | Lokasi |
| --- | --- |
| Domain, judul, description, About | origin, title, description, about dalam config/site.json |
| Publisher nyata | publisher dan publisherVerified; hanya isi berdasarkan identitas terverifikasi |
| URL APK | url dalam config/release.json |
| Versi, ukuran, Android, hash | Inspector APK |
| Screenshot dan urutannya | Array screenshots dalam config/site.json |
| Materi ulasan | demoPresentation.reviews |
| Markup dan CSS | src/presentation.mjs dan src/styles/site.css |
| Logo/favicon | public/assets/brand/ dan field ikon konfigurasi |
| Gambar WhatsApp | socialImage, JPEG 1200×630 pada folder brand |

## Update APK

Ubah URL HTTPS yang disetujui pemilik di release.json, lalu:

```bash
python3 scripts/inspect-apk.py --url --update-config
npm run check
node scripts/verify-download.mjs
```

Di Windows gunakan `python` jika tidak tersedia `python3`. Python standard library membaca AndroidManifest.xml biner dalam APK tanpa menjalankan aplikasi. Untuk file lokal, gunakan `python3 scripts/inspect-apk.py /path/release.apk --update-config`.

Inspector gagal jika versionName berupa resource reference atau SDK belum dikenali; selesaikan dengan Android aapt2 dan jangan menebak nilainya. Konfirmasi package dan checksum, lalu deploy. Endpoint menolak ukuran yang berbeda dari metadata release.

## Logo

Gunakan master persegi asli di assets/source/app-icon.png, turunan di public/assets/brand/, dan sesuaikan field konfigurasi. ICO/PNG 32×32 untuk favicon, PNG 180×180 untuk Apple, WebP untuk halaman. Ikon header Play Store tetap di public/assets/presentation/play-store.webp. Mengganti isi file pada path yang sama menghasilkan hash aset baru saat build.

## Urutan screenshot

| Nomor | Layar | File yang diberikan pemilik |
| --- | --- | --- |
| 1 | Launch | image(20261108-160850).png |
| 2 | Login | image(20261108-163532).png |
| 3 | Welcome bonus | image(20261108-160913).png |
| 4 | Game lobby | image(20261108-160933).png |
| 5 | First deposit | image(20261108-160920).png |
| 6 | Promotions | image(20261108-160943).png |
| 7 | Fast withdrawals | assets/source/07-withdrawals.jpg |

Gambar penuh sekitar 573×1280 (withdrawals 572×1280), tanpa crop yang mengubah konten penting. Thumbnail memiliki rasio sama. Banner withdrawals dikonfigurasi di `promoBanner` dalam `config/site.json`. Array konfigurasi menyimpan title, caption, src, thumbnailSrc, alt, width, height. Urutan carousel dan fullscreen mengikuti array yang sama. Gunakan screenshot asli dan dimensi yang benar.

## HTML lengkap

dist/readable/index.html adalah dokumen lengkap dengan head dan body berindentasi; salinannya ada pada html/index.html dalam kedua ZIP. dist/public/index.html adalah HTML minifikasi yang dikirim server. Sumber body berada di src/presentation.mjs, metadata di src/render.mjs, dan kerangka dokumen di src/templates/index.html.

Edit sumber lalu build ulang. Mengedit file hasil build tidak mengubah renderer dan akan tertimpa build berikutnya. Pengujian fingerprint melindungi teks, susunan body dan CSS asli presentasi; perubahan desain yang diminta di masa depan perlu baseline baru secara sadar.
