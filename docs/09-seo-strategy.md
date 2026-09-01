# SEO Strategy — Agar "Maheza Novrayuda" Muncul Teratas di Google

## Ekspektasi yang jujur dulu

Tidak ada perubahan teknis yang bisa **menjamin** posisi #1 di Google secara instan — itu bergantung pada waktu indexing (biasanya beberapa minggu), kompetisi nama (untungnya "Maheza Novrayuda" adalah nama yang cukup unik, hasil pencarian saat ini didominasi profil generik seperti ZoomInfo/RocketReach, bukan pesaing kuat), dan konsistensi update konten. Yang bisa dijamin: checklist di bawah ini **memaksimalkan peluang** secara nyata karena mengikuti praktik SEO teknis standar.

## 1. Technical SEO — fondasi wajib

### a. Title & meta description yang selalu memuat nama lengkap
```html
<!-- base.html -->
<title>{% block title %}Maheza Novrayuda — AI & Data Engineering Portfolio{% endblock %}</title>
<meta name="description" content="{% block meta_description %}Portofolio Maheza Novrayuda, mahasiswa Teknik Informatika fokus AI, Data Science, dan Data Engineering. Lihat project machine learning, RAG, dan analisis data.{% endblock %}">
```
Setiap halaman (`about.html`, `projects.html`, dsb.) harus override `title` dengan variasi yang tetap memuat nama, contoh: `{% block title %}Tentang Maheza Novrayuda{% endblock %}`.

### b. JSON-LD structured data `Person` — sinyal kuat untuk Google Knowledge Panel
Tambahkan di `<head>` `base.html` (isi dengan data asli dari `profile`):
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Maheza Novrayuda",
  "url": "https://mahezanovrayuda.com",
  "image": "https://mahezanovrayuda.com{{ profile.avatar.url }}",
  "jobTitle": "Informatics Engineering Student / AI & Data Enthusiast",
  "affiliation": {
    "@type": "CollegeOrUniversity",
    "name": "Universitas Putra Indonesia YPTK Padang"
  },
  "sameAs": [
    "https://www.linkedin.com/in/mahezanovrayuda",
    "https://github.com/MAHEZANOVRAYUDA"
  ]
}
</script>
```
`sameAs` ini **kunci utama** — Google memakainya untuk menghubungkan situs kamu dengan profil LinkedIn/GitHub sebagai entitas yang sama, memperkuat identitas nama di hasil pencarian.

### c. `sitemap.xml` dan `robots.txt`
```python
# portfolio/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Project

class ProjectSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    def items(self): return Project.objects.all()
    def location(self, obj): return f'/projects/{obj.pk}/'

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'
    def items(self): return ['portfolio:home', 'portfolio:about', 'portfolio:projects', 'portfolio:contact']
    def location(self, item):
        from django.urls import reverse
        return reverse(item)
```
```python
# config/urls.py — tambahkan
from django.contrib.sitemaps.views import sitemap
from portfolio.sitemaps import ProjectSitemap, StaticViewSitemap

urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': {'projects': ProjectSitemap, 'static': StaticViewSitemap}}),
]
```
Buat `static/robots.txt`:
```
User-agent: *
Allow: /
Sitemap: https://mahezanovrayuda.com/sitemap.xml
```

### d. Open Graph lengkap (bukan hanya `og:title`/`og:description` seperti sekarang)
Tambahkan `og:image`, `og:url`, dan Twitter Card supaya link portofolio tampil bagus saat dibagikan di LinkedIn/Twitter/WhatsApp:
```html
<meta property="og:image" content="https://mahezanovrayuda.com{% static 'img/og-cover.png' %}">
<meta property="og:url" content="https://mahezanovrayuda.com{{ request.path }}">
<meta name="twitter:card" content="summary_large_image">
```
Siapkan 1 gambar `og-cover.png` (1200×630px) berisi nama + tagline — desain sederhana di Figma/Canva.

## 2. Performance SEO (Core Web Vitals)

Google secara eksplisit memakai kecepatan situs (LCP, CLS, INP) sebagai faktor ranking. Ini terhubung langsung ke `02-frontend.md`:
- Migrasi dari Tailwind CDN → build (dampak performa paling besar)
- Compress gambar via Cloudinary transform (`f_auto,q_auto`)
- Lazy-load gambar di bawah fold: `<img loading="lazy">`

## 3. Off-page SEO — backlink & sinyal eksternal (paling berdampak untuk ranking nama)

Ini bagian yang **tidak bisa dikerjakan Antigravity lewat kode** — perlu aksi manual dari Maheza:

1. **Konsistensi profil di semua platform**: pastikan URL portofolio (`mahezanovrayuda.com`) dicantumkan di bio LinkedIn, GitHub profile README (sudah ada placeholder "`[Optional: Link to your personal website]`" di README GitHub kamu — isi ini!), dan platform lain (Dicoding, CodePolitan jika ada kolom profil).
2. **Google Search Console**: daftarkan domain, submit `sitemap.xml` secara manual, request indexing halaman utama — ini mempercepat proses indexing dari berbulan-bulan jadi hitungan hari/minggu.
3. **Bing Webmaster Tools**: sering dilewatkan, tapi bisa membantu visibilitas tambahan.
4. **Konsistensi nama**: gunakan ejaan nama yang sama persis ("Maheza Novrayuda") di semua platform — variasi ejaan memecah sinyal SEO.

## 4. Content marketing jangka menengah (opsional tapi berdampak besar)

Cara paling efektif jangka panjang untuk "menang" di pencarian nama adalah **punya lebih banyak konten berkualitas dengan nama kamu sebagai penulis**:
- Tulis artikel teknis (mis. "Cara Membangun RAG Pipeline dari Nol") di portofolio sendiri (lihat opsi `BlogPost` di `05-system-design.md`) atau di Medium/Dev.to dengan link balik ke portofolio.
- Setiap artikel = 1 halaman terindeks baru yang memuat nama kamu → memperkuat "personal SEO footprint".

## 5. Checklist ringkas eksekusi Antigravity

- [ ] Title & meta description tiap halaman memuat "Maheza Novrayuda"
- [ ] JSON-LD `Person` schema di `base.html`
- [ ] `sitemap.xml` + `robots.txt` aktif
- [ ] Open Graph image lengkap
- [ ] Core Web Vitals dioptimasi (lihat `02-frontend.md`)
- [ ] (Manual oleh Maheza) Submit ke Google Search Console setelah domain live
- [ ] (Manual oleh Maheza) Update link portofolio di bio LinkedIn & README GitHub
