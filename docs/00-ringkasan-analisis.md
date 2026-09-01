# Ringkasan Analisis — Portofolio Maheza Novrayuda

> Dibuat oleh: peran gabungan Frontend/Backend/Architect/Security/System Design/DevOps.
> Dokumen ini adalah **peta jalan** untuk seluruh file `.md` lain di paket ini. Berikan semua file ini ke Antigravity secara berurutan (00 → 10) agar konteksnya tidak hilang antar sesi.

## 1. Apa yang sudah ada (kondisi saat ini)

Stack yang terdeteksi dari source code:

| Layer | Teknologi |
|---|---|
| Backend | Django 5.2 (Python), `python-decouple`, `dj-database-url` |
| Database | SQLite (dev) → PostgreSQL via `DATABASE_URL` (prod) |
| Media storage | Cloudinary (`django-cloudinary-storage`) |
| Static files | WhiteNoise + `collectstatic` |
| Frontend | Django Template + **Tailwind via CDN** (`<script src="cdn.tailwindcss.com">`) + AOS (animate-on-scroll) |
| Deployment target | Vercel (`vercel.json` pakai builder `@vercel/python`, versi lama) |
| App | `portfolio` — models: `Profile`, `Project`, `Skill`, `Achievement`, `Certificate`, `Education`, `ContactMessage` |
| Halaman | Home, About, Projects, Project Detail, Contact |

Ini **arsitektur yang solid untuk skala personal portfolio** — model data sudah cukup lengkap (Profile singleton, Project dengan M2M Skill, Achievement, Certificate, Education). Masalah utama bukan di struktur data, tapi di:

1. **Konten** — masih placeholder generik ("AI Engineer & Data Enthusiast" tanpa detail nyata tentang kamu).
2. **Frontend production-readiness** — Tailwind CDN tidak boleh dipakai di production (lambat, tidak bisa purge CSS, banner warning di console).
3. **Konfigurasi Vercel usang** — format `builds`/`routes` di `vercel.json` adalah format Vercel v2 lama; Vercel modern pakai `@vercel/python` sebagai *Serverless Function* dengan struktur berbeda, dan Django + Vercel serverless punya keterbatasan (tidak cocok untuk migrasi DB otomatis, tidak ada persistent disk).
4. **Belum ada strategi SEO** untuk nama kamu bisa muncul di halaman pertama Google.
5. **Keamanan dasar** belum lengkap (security headers, `ALLOWED_HOSTS = ['*']`, secret key handling, dsb).

## 2. Data nyata tentang kamu (hasil riset publik)

Karena LinkedIn full profile tidak bisa diakses otomatis (dibatasi robots.txt), data berikut diambil dari **cuplikan hasil pencarian publik LinkedIn** dan **halaman GitHub profile README kamu sendiri** (yang sudah publik dan bisa diakses langsung):

- **Nama**: Maheza Novrayuda
- **Status**: Mahasiswa Teknik Informatika, Universitas Putra Indonesia YPTK Padang
- **Lokasi**: Padang, Sumatera Barat
- **Fokus**: AI/Machine Learning, Data Science, Data Engineering, NLP, Generative AI (RAG)
- **Tagline LinkedIn**: "Artificial Intelligent and Data enthusiast | undergraduate Informatics engineering at University of Putra Indonesia YPTK Padang"
- **Pengalaman/organisasi yang tercatat publik**: CodePolitan, Dicoding Academy, Digistar Club by Telkom Indonesia, Indigo Telkom
- **GitHub**: [github.com/MAHEZANOVRAYUDA](https://github.com/MAHEZANOVRAYUDA) — 16 repository publik, bio "puh masih pemula puh", README profile sudah berisi tabel tech stack rapi
- **Repo unggulan yang layak ditampilkan di portofolio**:
  - `RAG-BCA` — Retrieval-Augmented Generation pipeline (LLM + vector embedding + semantic search)
  - `CNN_CatvDog` / `CNN-for-prediction-cat-ot-dog` — CNN image classifier
  - `SentimentAnalysis` — NLP sentiment analysis dengan web interface
  - `AI-ML_DL-Project-Portofolio` — kumpulan multi-case AI/ML (EDA, feature engineering, benchmarking)
  - `Credit_Risk_Analysis` / `credit-risk-analysis` — ML pipeline prediksi risiko kredit
  - `Regression_HomePricingStreamlit` — regresi harga rumah + dashboard Streamlit
  - `DSF-dibimbing` — project AI/ML dari bootcamp Dibimbing
  - `data_wragling`, `End-to-end-machine-learning`

**Catatan penting**: karena saya tidak bisa login/scraping penuh LinkedIn kamu, sebagian detail (pengalaman kerja lengkap dengan tanggal, sertifikasi resmi, deskripsi tiap role) **perlu kamu isi/koreksi sendiri** saat mengisi Django Admin. Dokumen `01-content-strategy.md` sudah saya susun sebagai draf siap pakai berdasarkan data di atas — silakan sunting sebelum publish.

## 3. Urutan eksekusi yang direkomendasikan untuk Antigravity

1. `01-content-strategy.md` — isi ulang seed data / fixtures Profile, Project, Skill, Achievement
2. `02-frontend.md` — migrasi Tailwind CDN → build pipeline, refresh UI/UX
3. `03-backend.md` — perbaikan model, form, validasi, admin
4. `04-architecture.md` — struktur project & keputusan arsitektur
5. `05-system-design.md` — alur data, skalabilitas, caching
6. `06-security.md` — hardening
7. `07-devops.md` — CI/CD, testing, monitoring
8. `08-deployment-vercel.md` — langkah deploy nyata ke Vercel + database
9. `09-seo-strategy.md` — supaya nama kamu naik ranking Google
10. `10-roadmap-eksekusi.md` — checklist tahap demi tahap, bisa langsung dieksekusi Antigravity sebagai task list

## 4. Batasan penting yang harus diketahui dari awal

- **Django + Vercel serverless functions bisa jalan**, tapi punya batasan: tidak ada persistent filesystem (upload harus ke Cloudinary — untungnya sudah dipakai), cold start, dan **migrasi database tidak otomatis jalan saat deploy** (harus dijalankan manual/CI). Ini dibahas detail di `08-deployment-vercel.md`, termasuk alternatif (Railway/Render) jika Vercel terasa terlalu terbatas untuk Django.
- Target "nama saya muncul di posisi teratas Google" **tidak bisa dijamin 100%** oleh perubahan teknis semata — itu bergantung juga pada backlink, waktu (indexing butuh minggu–bulan), dan seberapa unik namamu di hasil pencarian. Tapi strategi teknis di `09-seo-strategy.md` akan memaksimalkan peluangnya.
