# GetWise – kalkulator keuangan Indonesia (situs statis)

## Struktur
- `src/content.py` – teks semua kalkulator, kategori, halaman Tentang/Kontak/Privasi/Syarat
- `src/static/js/finance.js` – mesin hitung (PPh 21 TER, BPJS, KPR, dll). Aturan ada di `RULES` di atas file
- `src/static/js/pages/*.js` – tampilan hasil per kalkulator
- `src/build.py` – membangun situs ke `dist/`
- `tests/test.js` – uji rumus (`node tests/test.js`)

## Membangun
    pip install jinja2
    SITE_BASE=https://domainanda.com ADSENSE=ca-pub-XXXX GA_ID=G-XXXX CONTACT_EMAIL=halo@domainanda.com python src/build.py

## Deploy ke Cloudflare Pages (gratis)
1. Unggah folder ini ke repo GitHub baru.
2. Cloudflare → Workers & Pages → Create → Pages → Connect to Git → pilih repo.
3. Build command: `pip install jinja2 && python src/build.py`  ·  Build output directory: `dist`
4. Environment variables: `SITE_BASE`, `CONTACT_EMAIL` (lalu `ADSENSE`, `GA_ID` saat sudah ada). Isi `PYTHON_VERSION` = `3.12`.
5. Custom domains → tambahkan domain Anda.

Alternatif tanpa Git: jalankan build di komputer, lalu Cloudflare Pages → "Upload assets" → seret folder `dist`.

## Memperbarui aturan
Ubah `RULES` di `finance.js` (mis. batas upah JP tiap Maret), jalankan `node tests/test.js`, ubah `RULES_UPDATED` di `build.py`, lalu build ulang.
