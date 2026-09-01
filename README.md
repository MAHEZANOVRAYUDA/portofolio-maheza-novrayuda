# 🚀 Maheza Novrayuda - Professional AI & Data Engineering Portfolio

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=flat&logo=django)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)
![HTMX](https://img.shields.io/badge/HTMX-336699?style=flat&logo=htmx&logoColor=white)
![Vercel](https://img.shields.io/badge/Deployed_on-Vercel-000000?style=flat&logo=vercel&logoColor=white)

Website portofolio profesional dan interaktif yang dibangun khusus untuk menampilkan keahlian, proyek, dan pencapaian di bidang **Artificial Intelligence (AI)** dan **Data Engineering**.

Sistem ini didesain dengan fokus ekstrim pada **Performa (Core Web Vitals)**, **SEO Tingkat Lanjut**, dan **User Experience (UX)**.

---

## ✨ Fitur Utama (Key Features)

### 1. ⚡ SPA-Like Experience dengan HTMX
Perpindahan antarahalaman tidak memerlukan *full-page reload*. Aplikasi menggunakan **HTMX** (`hx-boost`) dan **NProgress** untuk memberikan transisi instan dan super responsif yang terasa persis seperti *Single Page Application* (React/Next.js) namun tetap mempertahankan kekuatan SEO server-side rendering dari Django.

### 2. 🔍 SEO Dominance (Google #1 Ranking Strategy)
*   **JSON-LD Structured Data**: Skema khusus tipe `Person` yang secara otomatis memberi tahu bot Google bahwa situs ini dimiliki oleh entitas Maheza Novrayuda (AI & Data Engineer).
*   **Sitemap Otomatis**: Dilengkapi dengan `sitemap.xml` dinamis menggunakan `django.contrib.sitemaps`.
*   **Meta & Open Graph (OG) Tags**: Optimasi mendalam pada `<title>`, meta description, serta *Twitter Cards* untuk memastikan *preview* tautan terlihat sempurna di LinkedIn, WhatsApp, dll.
*   **Semantic HTML**: Penggunaan tag HTML5 dan hierarki heading yang ramah mesin pencari.

### 3. 🚄 High-Performance Architecture
*   **WhiteNoise Compression**: File statis (CSS/JS) dikompres (Brotli/Gzip) dan diberi *cache-busting* otomatis dengan `CompressedManifestStaticFilesStorage`.
*   **Local Memory Caching**: Django menggunakan *LocMemCache* di latar belakang untuk mempercepat *response time*.
*   **Asynchronous Contact Form**: Pengiriman email dari halaman kontak ditangani dalam *background thread* terpisah (`threading`), sehingga notifikasi terkirim seketika kepada pengguna tanpa mengalami proses menunggu dari SMTP server.
*   **Font Preloading & Lazy Loading Images**: Optimasi *Critical Rendering Path* untuk memastikan halaman bisa mulai berinteraksi seketika.

### 4. 💎 Desain UI/UX Premium
*   **Glassmorphism & Particle Animations**: Desain latar belakang yang reaktif dengan AOS (Animate On Scroll) memastikan setiap scroll pengguna terasa interaktif.
*   **Tailwind CSS**: Styling modern menggunakan sistem *utility-first* dengan konfigurasi khusus (misal warna `sky` dan font kustom `Inter` & `Outfit`).

---

## 🛠️ Tech Stack (Teknologi yang Digunakan)

- **Backend**: Python 3.x, Django 5+
- **Frontend**: HTML5, Vanilla JavaScript, Tailwind CSS, HTMX, NProgress
- **Database**: PostgreSQL (Via `dj_database_url`)
- **Storage**: Cloudinary (Media files & Images)
- **Deployment**: Vercel Serverless (dengan skrip `build_files.sh`)

---

## 🚀 Cara Menjalankan di Lokal (Local Development)

1. **Clone repository ini:**
   ```bash
   git clone https://github.com/username/portofolio-maheza-novrayuda.git
   cd portofolio-maheza-novrayuda
   ```

2. **Buat Virtual Environment & Install Dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Untuk Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Atur Environment Variables:**
   Buat file `.env` di root direktori berdasarkan `.env.example`:
   ```ini
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   CLOUDINARY_URL=cloudinary://API_KEY:API_SECRET@CLOUD_NAME
   ```

4. **Migrasi Database & Buat Superuser:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Jalankan Server:**
   ```bash
   python manage.py runserver
   ```
   Akses `http://127.0.0.1:8000/` di browser Anda. Untuk login admin, buka `http://127.0.0.1:8000/admin/`.

---

## ☁️ Deployment (Vercel)

Proyek ini telah dikonfigurasi secara optimal untuk di-deploy ke **Vercel** menggunakan `vercel.json` dan skrip `build_files.sh`.

Setiap kali ada kode yang di-*push* atau di-*merge* ke branch `main` di GitHub, Vercel akan otomatis melakukan proses *build*, kompresi WhiteNoise, dan menerbitkannya secara live ke publik!

---

*Desain dan Rekayasa Sistem oleh [Maheza Novrayuda](https://mahezanovrayuda.com)*.
