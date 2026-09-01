# Deployment — Vercel (Django) Langkah demi Langkah

## 1. Perbaiki `vercel.json` — format lama sudah usang

Versi saat ini pakai skema `builds`/`routes` gaya lama:
```json
{
  "version": 2,
  "builds": [{ "src": "config/wsgi.py", "use": "@vercel/python" }],
  "routes": [
    { "src": "/static/(.*)", "dest": "/static/$1" },
    { "src": "/(.*)", "dest": "config/wsgi.py" }
  ]
}
```

Ganti dengan skema modern (`rewrites` + `functions`), dan arahkan entrypoint ke file WSGI yang benar:

```json
{
  "buildCommand": "bash build_files.sh",
  "outputDirectory": "staticfiles",
  "rewrites": [
    { "source": "/(.*)", "destination": "config/wsgi.py" }
  ]
}
```

> Catatan penting: dukungan Python di Vercel **berubah dari waktu ke waktu** dan pernah mengalami perubahan kebijakan runtime. Sebelum Antigravity mengeksekusi ini, **cek dokumentasi resmi Vercel Python Runtime terbaru** (`vercel.com/docs/functions/runtimes/python`) karena format `vercel.json` bisa saja sudah berubah lagi sejak dokumen ini ditulis. Jika terjadi error deploy terkait runtime, itu tandanya perlu menyesuaikan ke format terbaru mereka.

## 2. Environment Variables yang wajib diset di Vercel Dashboard

Project Settings → Environment Variables:

| Key | Contoh nilai | Keterangan |
|---|---|---|
| `SECRET_KEY` | (generate baru, jangan pakai default) | `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DEBUG` | `False` | wajib False di production |
| `ALLOWED_HOSTS` | `mahezanovrayuda.com,www.mahezanovrayuda.com,*.vercel.app` | lihat `06-security.md` |
| `DATABASE_URL` | `postgres://...` (dari Neon/Supabase/Railway, pakai **pooler endpoint**) | lihat §3 |
| `CLOUDINARY_URL` | `cloudinary://<api_key>:<api_secret>@<cloud_name>` | dari dashboard Cloudinary |
| `EMAIL_HOST_PASSWORD` dll | (sesuai provider email dipilih) | untuk notifikasi contact form |
| `ADMIN_URL` | (path custom, opsional) | lihat `06-security.md` |
| `SENTRY_DSN` | (opsional) | untuk error tracking |

## 3. Setup database PostgreSQL gratis (pilih salah satu)

Karena Vercel serverless tidak punya disk persisten, SQLite **tidak akan berfungsi** di production. Pilihan gratis yang direkomendasikan (urut dari paling mudah diintegrasikan dengan serverless):

1. **Neon** (neon.tech) — Postgres serverless, auto-scaling, ada connection pooler bawaan. Cocok banget dengan arsitektur Vercel serverless.
2. **Supabase** — Postgres + dashboard admin visual, free tier cukup untuk portofolio.
3. **Railway** — Postgres biasa dengan free trial credit.

Langkah umum:
1. Buat project baru di provider pilihan → copy connection string (pastikan pakai **pooled connection** jika tersedia, biasanya ada opsi `?pgbouncer=true` atau host khusus `-pooler`).
2. Paste ke env var `DATABASE_URL` di Vercel.
3. Jalankan migrasi (lihat `07-devops.md` §3) menunjuk ke database ini.

## 4. Custom domain — penting untuk kepercayaan & SEO

1. Beli domain (rekomendasi: `mahezanovrayuda.com` atau `.dev` — nama domain yang sama persis dengan nama kamu adalah sinyal SEO terbaik untuk pencarian nama).
2. Di Vercel: Project → Settings → Domains → tambahkan domain, ikuti instruksi DNS (biasanya tambah record `A`/`CNAME` di registrar).
3. Setelah domain aktif, update `ALLOWED_HOSTS` dan `CSRF_TRUSTED_ORIGINS`:
   ```python
   CSRF_TRUSTED_ORIGINS = ['https://mahezanovrayuda.com', 'https://www.mahezanovrayuda.com']
   ```

## 5. Checklist sebelum go-live

- [ ] `DEBUG=False` di production env
- [ ] `python manage.py check --deploy` tidak ada warning kritikal
- [ ] Migrasi database sudah dijalankan ke DB production
- [ ] Superuser admin sudah dibuat (`python manage.py createsuperuser` — jalankan lewat local dengan `DATABASE_URL` production, karena tidak ada shell interaktif di Vercel)
- [ ] Semua data seed (`01-content-strategy.md`) sudah diisi lewat `/admin/`
- [ ] Custom domain aktif dengan HTTPS (Vercel otomatis provide SSL certificate)
- [ ] Uji form contact benar-benar mengirim & tersimpan
- [ ] Cek Lighthouse score (target: Performance & SEO > 90)

## 6. Alternatif jika Vercel terasa terlalu terbatas untuk Django

Vercel didesain utamanya untuk Next.js/frontend; dukungan Python-nya adalah *serverless function*, bukan server Django yang "hidup" terus. Jika ke depan Antigravity/Maheza menemukan keterbatasan (mis. butuh WebSocket, background job, atau migrasi otomatis yang lebih mulus), alternatif yang **tetap punya free tier dan lebih native untuk Django**:
- **Railway** — deploy langsung dari GitHub, database Postgres built-in, tidak perlu ubah `vercel.json`-style config.
- **Render** — mirip Railway, punya "Web Service" untuk Django + "PostgreSQL" addon.

Ini tidak wajib dilakukan sekarang — cukup dicatat sebagai *fallback plan* karena user secara eksplisit meminta Vercel.
