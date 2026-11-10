# Metadata, robots, sitemap dan kampanye

| Elemen | Implementasi |
| --- | --- |
| Judul | `JAIHO777 – Official Android APK Download`, sesuai konfigurasi sebelumnya |
| Description | `Explore JAIHO777 for Android. View app information, installation instructions, and download the official APK directly.` |
| Bahasa / locale | `en-IN` / `en_IN` |
| Canonical | URL HTTPS bersih tanpa UTM, dari origin konfigurasi |
| Open Graph | title, description, URL, site name, locale, JPEG 1200×630, tipe dan alt gambar |
| Twitter | summary_large_image dengan judul, description dan gambar yang sama |
| Favicon | ICO, PNG 32×32 dan Apple 180×180 |
| JSON-LD | SoftwareApplication dan WebSite dengan metadata file nyata |
| Sitemap | `/sitemap.xml`, halaman utama dan `/privacy/`, lastmod dari updatedAt |
| Robots | `/robots.txt`, sesuai mode presentasi, dengan URL sitemap |
| Error | 404/503 dengan noindex tanpa rincian internal |

Preview WhatsApp membutuhkan URL/gambar yang bisa diakses crawler. Site private atau sign-in wall dapat menghalangi preview. WhatsApp dapat menyimpan preview lama; URL gambar berhash membantu pembaruan, tetapi waktu cache bukan kendali halaman.

## Listing aktif

Dengan `demoPresentation.enabled: true`, rating, badge Verified App, dan ulasan tetap tampil tanpa label DEMO. Metadata menggunakan `index,follow,max-image-preview:large`. Robots mengizinkan pengambilan halaman informasi, mengecualikan `/download` serta `/api/`, dan mencantumkan lokasi sitemap pada origin yang dikonfigurasi.

Rating/review dan jumlah unduhan tidak dimasukkan ke structured data. Robots bukan pengaman source; akses file diatur router server.

## Tautan kampanye

```text
https://download.example.com/?utm_source=whatsapp&utm_medium=broadcast&utm_campaign=nov-presentation&utm_content=message-a
https://download.example.com/?utm_source=sms&utm_medium=sms&utm_campaign=nov-presentation&utm_content=message-b
```

Ganti domain. Allowlist: utm_source, utm_medium, utm_campaign, utm_content, utm_term, utm_id, campaign_id, source, ref. Maksimal 100 karakter per nilai. Karakter kontrol, email yang jelas, digit panjang dan URL bersarang ditolak.

Label diteruskan oleh server ke request `/download`, termasuk tanpa JavaScript. Label tidak dikirim ke URL asal CDN. Tab storage dapat mempertahankan label maksimal 30 menit. Tidak ada cookie iklan/pengenal persisten. DNT/GPC mematikan penyimpanan sementara dan metrik aplikasi. Hosting/CDN tetap dapat memproses data koneksi biasa.

Jangan menaruh nomor telepon, UID orang, email, password atau token dalam link. Filter bukan pengganti pengelolaan data pribadi.

## Analytics opsional

Analytics tetap mati: `analytics.enabled: false`. Atribusi dipertahankan, tetapi dashboard pelaporan tidak disediakan tanpa backend metrik. Tidak ada script analytics pihak ketiga.

Untuk hitungan agregat pada Cloudflare, buat dataset Analytics Engine dan binding:

```toml
[[analytics_engine_datasets]]
binding = "ANALYTICS"
dataset = "jaiho777_campaigns"
```

Lalu aktifkan analytics.enabled, tinjau notice privasi, build dan deploy. Kode aplikasi hanya mengirim nama event, source, medium, campaign, content dan angka hitungan. Event download_request berarti respons APK mulai dikirim, bukan bukti download selesai, instalasi, registrasi atau deposit.

## Domain publik dan pengindeksan

Atur origin sebelum build. Untuk versi faktual yang hendak diindeks, gunakan Search Console akun pemilik domain dan kirim sitemap setelah memastikan crawler mendapat akses. Paket ini tidak mengirim Search Console otomatis dan tidak menjanjikan indeks/peringkat Google.

## Rujukan

- [Google robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
- [Google sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google canonical](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Cloudflare binding](https://developers.cloudflare.com/workers/wrangler/configuration/)
