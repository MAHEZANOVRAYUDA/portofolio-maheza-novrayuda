# Architecture — Keputusan Arsitektur

## 1. Gaya arsitektur

Ini adalah **monolith Django klasik** (server-rendered templates) — dan itu **pilihan yang tepat** untuk portofolio personal: satu developer, traffic rendah-menengah, tidak butuh microservices. Jangan pecah jadi API + SPA terpisah kecuali ada alasan konkret (mis. ingin belajar Next.js secara eksplisit).

```
┌─────────────────────────────────────────────┐
│                  Browser                      │
└───────────────────────┬───────────────────────┘
                         │ HTTPS
┌───────────────────────▼───────────────────────┐
│         Vercel Edge / Serverless Function       │
│   ┌─────────────────────────────────────────┐  │
│   │      Django (WSGI) — config/wsgi.py       │  │
│   │  ┌───────────┐  ┌───────────────────┐    │  │
│   │  │  urls.py  │→│  views.py (CBV)     │    │  │
│   │  └───────────┘  └─────────┬──────────┘    │  │
│   │                            │                │  │
│   │                   ┌────────▼────────┐       │  │
│   │                   │  models.py (ORM) │       │  │
│   │                   └────────┬────────┘       │  │
│   └────────────────────────────┼────────────────┘  │
└────────────────────────────────┼───────────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                     │
      ┌───────▼──────┐   ┌────────▼────────┐   ┌───────▼───────┐
      │  PostgreSQL   │   │   Cloudinary     │   │ WhiteNoise     │
      │ (Neon/Railway/│   │ (media: gambar,  │   │ (static files, │
      │  Supabase)    │   │  file certificate)│   │  di-bundle)    │
      └───────────────┘   └──────────────────┘   └────────────────┘
```

## 2. Kenapa komponen ini dipilih

| Komponen | Alasan |
|---|---|
| **Django** | Sudah dipakai, admin panel bawaan sangat cocok untuk Maheza mengelola konten (Project, Skill, Achievement) tanpa perlu bikin CMS custom |
| **PostgreSQL eksternal** (bukan SQLite) | Vercel serverless **tidak punya persistent disk** — SQLite akan reset tiap cold start. Wajib pakai Postgres terkelola (Neon, Supabase, atau Railway — semua ada free tier) |
| **Cloudinary** | Sudah terkonfigurasi dengan baik di `settings.py`; tepat karena serverless juga tidak bisa simpan file upload lokal |
| **WhiteNoise** | Melayani static file (CSS/JS/font) langsung dari aplikasi Django tanpa perlu CDN terpisah — cukup untuk skala portofolio |

## 3. Batasan arsitektur yang perlu disadari

- **Vercel serverless function punya cold start** (~1-3 detik untuk request pertama setelah idle). Untuk portofolio ini bisa diterima, tapi jelaskan trade-off ini di `08-deployment-vercel.md` termasuk alternatif jika ingin selalu-cepat (Railway/Render yang punya server persisten).
- **Migrasi database tidak otomatis** di Vercel — harus dijalankan manual atau via CI step terpisah (dibahas di `07-devops.md` dan `08-deployment-vercel.md`).
- Tidak ada background job/queue di arsitektur ini — untuk skala portofolio, **tidak dibutuhkan**. Jangan tambahkan Celery/Redis kecuali benar-benar diperlukan (over-engineering).

## 4. Struktur folder yang direkomendasikan (evolusi dari yang sudah ada)

```
config/                # project settings (tetap)
portfolio/
├── models.py
├── views.py
├── forms.py
├── admin.py
├── urls.py
├── management/commands/seed_profile.py   # (baru — lihat 01-content-strategy.md)
├── tests/                                # (baru — lihat 03-backend.md §3)
│   ├── test_models.py
│   └── test_views.py
static/
├── css/
│   ├── input.css        # (baru — source Tailwind)
│   └── output.css       # (baru — hasil build, di-gitignore atau di-commit tergantung strategi CI)
templates/
scripts/
└── setup_project.py     # (sudah ada)
```

## 5. Prinsip desain yang dipegang di seluruh paket dokumen ini

1. **Jangan over-engineer** — semua rekomendasi di paket dokumen ini sengaja dijaga proporsional untuk portofolio personal, bukan sistem enterprise.
2. **Admin-first content management** — semua konten (project, skill, achievement) harus bisa diubah lewat `/admin/` tanpa deploy ulang kode.
3. **Serverless-aware** — semua keputusan (storage, DB, static files) mengasumsikan tidak ada persistent disk di production.
