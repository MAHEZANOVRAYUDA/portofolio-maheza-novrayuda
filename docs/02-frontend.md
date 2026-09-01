# Frontend — Revisi Tampilan & UX

## 1. Masalah utama saat ini

```html
<!-- templates/base.html -->
<script src="https://cdn.tailwindcss.com"></script>
```

Ini **Tailwind Play CDN** — resmi dinyatakan oleh Tailwind Labs **"not designed for production"**: tidak ada CSS purge (file jadi besar), compile di browser tiap request (lambat), dan sejak Tailwind v4 CDN build ini bahkan tertinggal fitur. Ini juga penyebab utama skor Lighthouse/PageSpeed jelek → berdampak ke SEO.

## 2. Rencana migrasi (untuk Antigravity eksekusi)

1. Install Tailwind CSS sebagai **build step**, bukan CDN:
   ```bash
   npm init -y
   npm install -D tailwindcss@latest postcss autoprefixer
   npx tailwindcss init -p
   ```
2. Buat `static/css/input.css`:
   ```css
   @import "tailwindcss";
   ```
3. Konfigurasi `tailwind.config.js` — pindahkan `theme.extend` yang sudah ada di `<script>` inline `base.html` (font `Inter`/`Outfit`, warna `primary #0ea5e9`, `accent #22c55e`, `dark #020617`, `surface #0b1220`) ke sini agar identitas visual tetap konsisten, tidak berubah drastis:
   ```js
   module.exports = {
     content: ['./templates/**/*.html', './portfolio/**/*.py'],
     theme: {
       extend: {
         fontFamily: { sans: ['Inter', 'sans-serif'], display: ['Outfit', 'sans-serif'] },
         colors: { primary: '#0ea5e9', accent: '#22c55e', dark: '#020617', surface: '#0b1220' },
       },
     },
   }
   ```
4. Build ke `static/css/output.css`:
   ```bash
   npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --minify
   ```
5. Ganti `<script src="cdn.tailwindcss.com">` di `base.html` dengan:
   ```html
   <link rel="stylesheet" href="{% static 'css/output.css' %}">
   ```
6. Tambahkan langkah build CSS ini ke `build_files.sh` (lihat `07-devops.md`) sebelum `collectstatic`, supaya otomatis jalan tiap deploy.

## 3. Perbaikan UX/UI berdasarkan referensi portofolio developer terbaik 2026

Riset dari beberapa showcase portofolio developer (Elementor, Colorlib, Portfolio Studio) menyimpulkan pola yang konsisten pada portofolio yang efektif — dan pola-pola ini bisa diadaptasi ke desain gelap/glassmorphism yang sudah kamu punya:

- **Formula 4-bagian yang terbukti efektif**: Hero (siapa kamu) → Karya/Project (apa yang bisa kamu buat) → Skill/Bukti → Cara menghubungi. Struktur `home.html` kamu sudah dekat dengan ini — pertahankan, jangan tambah section yang tidak perlu.
- **Kecepatan load < 2 detik** — pemicu utama recruiter bounce. Ini alasan #1 migrasi dari Tailwind CDN.
- **Mobile-first wajib** — banyak rekruter cek portofolio dari HP. Audit tiap halaman dengan Chrome DevTools device mode.
- **Custom domain** lebih dipercaya daripada subdomain `vercel.app` (dibahas di `08-deployment-vercel.md` & `09-seo-strategy.md`).
- **Deskripsi project harus scannable**: judul jelas, 2-3 kalimat masalah→solusi, badge teknologi, link demo & GitHub berdampingan (bukan hanya "lihat detail").
- **Restraint / kesederhanaan menang** — hindari terlalu banyak animasi AOS di setiap elemen; gunakan hanya untuk elemen kunci (hero, kartu project) agar tidak terasa "berat" atau mengganggu.

## 4. Checklist perbaikan konkret per halaman

### `base.html`
- [ ] Hapus Tailwind CDN, pakai build (lihat §2)
- [ ] Tambahkan `<link rel="canonical">` dinamis per halaman (lihat `09-seo-strategy.md`)
- [ ] Tambahkan JSON-LD `Person` schema di halaman home (lihat `09-seo-strategy.md`)
- [ ] Pastikan `favicon` dan `apple-touch-icon` ada (saat ini tidak terlihat di head)
- [ ] Tambahkan `<meta name="robots" content="index, follow">`

### `home.html`
- [ ] Hero: nama besar + tagline spesifik (bukan generik "AI Engineer") + CTA ganda: "Lihat Project" & "Hubungi Saya"
- [ ] Section featured projects: pastikan card menampilkan tech-stack badges dari `project.skills`
- [ ] Tambahkan bagian "GitHub Activity" opsional (embed statis, bukan iframe berat)

### `projects.html`
- [ ] Filter berdasarkan kategori Skill (`skills_by_category` sudah tersedia di context — tinggal render sebagai filter chip dengan Alpine.js atau vanilla JS)

### `project_detail.html`
- [ ] Tampilkan `metrics` secara menonjol (badge angka besar), bukan teks kecil
- [ ] Tombol "Previous/Next project" (sudah ada di context `prev_project`/`next_project`) — pastikan terlihat jelas di UI

### `about.html` & `contact.html`
- [ ] Tambahkan `Education` timeline (model sudah ada, context `educations` sudah dikirim — tinggal pastikan dirender)
- [ ] Form contact: tambahkan validasi client-side + honeypot anti-spam sederhana (lihat `06-security.md`)

## 5. Aksesibilitas (WCAG) — sering dilewatkan tapi berpengaruh ke citra profesional

- Kontras teks putih di atas background gelap harus dicek (khususnya teks abu-abu muda di atas `#020617`)
- Semua `<img>` wajib punya `alt` deskriptif (termasuk logo skill icon)
- Form input wajib punya `<label>` yang terasosiasi (`for`/`id`), bukan hanya placeholder
- Navigasi bisa diakses via keyboard (`tab`, `enter`)
