# Roadmap Eksekusi — Checklist Bertahap untuk Antigravity

Urutan ini dirancang supaya tiap tahap bisa langsung dijalankan, diuji, dan di-commit sebelum lanjut ke tahap berikutnya. Jangan loncat tahap — beberapa tahap saling bergantung (mis. security header butuh `DEBUG=False` yang sudah benar dari awal).

## Fase 1 — Konten & Data (tanpa risiko merusak apa pun)
1. Baca `01-content-strategy.md`
2. Buat `portfolio/management/commands/seed_profile.py` untuk isi data awal
3. Jalankan `python manage.py seed_profile` di local
4. Review hasil di `/admin/`, sesuaikan detail yang perlu dikoreksi Maheza

## Fase 2 — Backend hardening
1. Baca `03-backend.md`
2. Tambahkan honeypot + validasi form contact
3. Tambahkan `send_mail` notifikasi
4. Perkuat `admin.py` (list_display, filter, prepopulated_fields)
5. Tambahkan validator upload file
6. Tulis test dasar (`tests/test_models.py`, `tests/test_views.py`)
7. Jalankan `python manage.py test` — pastikan semua hijau

## Fase 3 — Frontend migration
1. Baca `02-frontend.md`
2. Setup Tailwind build pipeline (npm install, config, build CSS)
3. Ganti CDN script dengan `<link>` ke `output.css`
4. Verifikasi visual tidak berubah drastis (bandingkan screenshot before/after)
5. Terapkan checklist per halaman (home, projects, project_detail, about, contact)
6. Audit aksesibilitas dasar (alt text, label form, kontras warna)

## Fase 4 — Security
1. Baca `06-security.md`
2. Perbaiki `ALLOWED_HOSTS`
3. Tambahkan blok security headers untuk `DEBUG=False`
4. Tambahkan rate limiting form contact
5. Custom admin URL via env var

## Fase 5 — SEO
1. Baca `09-seo-strategy.md`
2. Update title/meta description tiap template
3. Tambahkan JSON-LD Person schema
4. Buat `sitemaps.py`, daftarkan di `urls.py`
5. Buat `robots.txt`
6. Buat OG image, lengkapi Open Graph tags

## Fase 6 — DevOps & CI
1. Baca `07-devops.md`
2. Update `build_files.sh`
3. Buat `.github/workflows/ci.yml`
4. Setup GitHub Secrets (`SECRET_KEY`, `DATABASE_URL`)
5. (Opsional) tambahkan Sentry

## Fase 7 — Deployment ke Vercel
1. Baca `08-deployment-vercel.md`
2. Buat database Postgres gratis (Neon/Supabase)
3. Update `vercel.json` ke format modern — **cek dokumentasi Vercel Python terbaru dulu**
4. Set semua environment variables di Vercel Dashboard
5. Deploy, jalankan migrasi ke DB production
6. Buat superuser, isi ulang seed data via `/admin/` production
7. Sambungkan custom domain
8. Jalankan checklist go-live di `08-deployment-vercel.md` §5

## Fase 8 — Pasca-launch (aksi manual Maheza, di luar kemampuan Antigravity)
1. Submit sitemap ke Google Search Console
2. Update link portofolio di bio LinkedIn & README GitHub
3. Pantau Vercel Analytics & Sentry selama 1-2 minggu pertama
4. Update konten project secara berkala (setiap project baru selesai → tambahkan ke portofolio)

---

**Prinsip kerja untuk Antigravity di setiap fase**: commit kecil & sering, jalankan test sebelum commit, jangan gabungkan perubahan dari fase berbeda dalam satu commit besar. Jika ragu terhadap detail teknis yang berubah cepat (mis. format `vercel.json`), selalu verifikasi ke dokumentasi resmi terbaru sebelum eksekusi, karena dokumen ini dibuat pada satu titik waktu dan platform seperti Vercel bisa berubah.
