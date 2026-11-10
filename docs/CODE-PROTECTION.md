# Perlindungan source dan batasnya

HTML, CSS, JavaScript dan gambar yang dikirim ke browser dapat dilihat/disimpan/disalin. Tidak ada metode web yang menjadikannya sepenuhnya tidak bisa diambil. Minifikasi mengurangi ukuran dan menyulitkan pembacaan langsung, bukan enkripsi.

| Lapisan | Implementasi |
| --- | --- |
| Router | Hanya halaman yang ditentukan dan allowlist aset hasil build dilayani |
| File privat | src, config, Git, lockfile, ZIP source dan dokumen internal tidak memiliki route publik |
| APK asal | URL berada dalam konfigurasi/bundle server, bukan HTML/JS browser |
| Target download | Query pengunjung tidak dapat mengganti URL sumber |
| Source map | Tidak dibuat dan tidak dipublikasikan |
| Browser assets | HTML/CSS/JS minifikasi, nama berhash, ETag |
| Header browser | CSP origin sendiri, nosniff, frame protection, pembatasan permission |
| Transport | HTTPS dan HSTS, redirect HTTP ke HTTPS |
| Error | Tanpa stack trace atau rincian source internal |

Download menolak redirect asal, MIME tidak sesuai, ukuran penuh berbeda dan range tidak konsisten. Ukuran bukan bukti isi sama: cek file nyata memakai SHA-256. Hash penuh tidak dihitung pada setiap request agar streaming tidak terhambat; gunakan source release tetap dan inspeksi ulang saat memperbarui file.

Simpan source ZIP/repository dengan akses yang Anda kendalikan. Bundle dist/server/index.js diunggah sebagai modul eksekusi Worker, bukan file statis untuk diunduh atau dimuat lewat script tag. Jangan unggah seluruh proyek ke direktori publik. Pada host lain, pertahankan batas server/publik dan uji path privat kembali.

Robots bukan pengaman akses; halaman private memerlukan pengendalian akses hosting. Tidak ada pemblokiran klik kanan, seleksi teks, keyboard atau Developer Tools karena tidak melindungi kode dan dapat mengganggu Android. Bila menambahkan kredensial, simpan sebagai secret runtime server, bukan HTML, JavaScript atau config/site.json.
