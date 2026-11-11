# Deploy ke Cloudflare — realcashgame.app

Pakai paket **JAIHO777-deploy.zip**. Domain utama: `https://realcashgame.app`.

## 1. Siapkan akun

1. Domain `realcashgame.app` sudah ada di Cloudflare (DNS di Cloudflare).
2. Install Node.js 22+.
3. Login Wrangler:
   ```bash
   npx wrangler login
   ```

## 2. Deploy

```bash
# ekstrak ZIP
unzip JAIHO777-deploy.zip -d jaiho777-deploy
cd jaiho777-deploy

# deploy Worker
npx wrangler deploy
```

Tidak perlu `npm install` atau `npm run build`. Bundle sudah siap.

## 3. Pasang custom domain

Di Cloudflare Dashboard:

1. Workers & Pages → pilih worker `jaiho777-apk-download` (atau nama di `wrangler.toml`)
2. Settings → Domains & Routes → Add → Custom Domain
3. Isi: `realcashgame.app` (dan opsional `www.realcashgame.app`)

Pastikan DNS A/CNAME untuk domain itu dikelola Cloudflare.

Opsional di `wrangler.toml`:

```toml
workers_dev = false
routes = [
  { pattern = "realcashgame.app", custom_domain = true }
]
```

Lalu `npx wrangler deploy` lagi.

## 4. Cek setelah live

```bash
curl -I 'https://realcashgame.app/'
curl -I 'https://realcashgame.app/robots.txt'
curl -I 'https://realcashgame.app/sitemap.xml'
curl -I 'https://realcashgame.app/download'
curl --fail 'https://realcashgame.app/download' -o jaiho777-check.apk
```

Harus:

- `/` → 200, HTML listing
- `/robots.txt` → Allow `/`, Disallow `/download` dan `/api/`
- `/sitemap.xml` → `https://realcashgame.app/` dan `/privacy/`
- `/download` → APK attachment, ~47.5 MB
- Canonical & Open Graph memakai `https://realcashgame.app`

## 5. Kalau mau ubah konten lagi

Pakai **source.zip**, set `origin` di `config/site.json` ke `https://realcashgame.app`, lalu:

```bash
npm ci
npm run check
npx wrangler deploy
```

Atau satu kali build:

```bash
npm run build -- --origin=https://realcashgame.app
```

## Catatan

- Favicon = ikon Google Play
- Ikon app di listing tetap logo JAIHO777
- Tombol Install mengarah langsung ke APK CloudFront
- Halaman WhatsApp / Play listing: `https://realcashgame.app/`
- Halaman SMS (tema UPI / bank withdrawal): `https://realcashgame.app/sms/`
- Contoh link blast SMS: `https://realcashgame.app/sms/?utm_source=sms&utm_medium=sms&utm_campaign=nama-kampanye`
