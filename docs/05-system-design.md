# System Design — Alur Data, Caching, Skalabilitas

## 1. Alur data utama

### Request halaman Home
```
1. Browser GET /
2. Vercel routes → Django WSGI
3. HomeView.get_queryset() → SELECT * FROM Project
4. get_context_data():
   - Profile.objects.first()          → 1 query
   - Skill.objects.all()              → 1 query, di-loop di Python (lihat 03-backend.md)
   - Project.objects.filter(featured) → 1 query
   - Achievement.objects.filter(...)  → 1 query
   - Certificate.objects.filter(...)  → 1 query
5. Render template home.html
6. Response HTML → browser
```
Total ±6 query per load Home. Untuk traffic portofolio personal (puluhan-ratusan visitor/hari), ini **tidak masalah** sama sekali secara performa. Optimasi caching di bawah ini sifatnya *nice-to-have* untuk masa depan, bukan kebutuhan mendesak.

### Alur submit form Contact
```
1. Browser POST /contact/
2. ContactForm divalidasi (CSRF token wajib — Django default sudah aktif)
3. form_valid() → simpan ContactMessage ke DB
4. (baru) → kirim email notifikasi ke Maheza
5. Redirect ke /contact/ dengan Django messages "Terima kasih..."
```

## 2. Caching (opsional, terapkan jika traffic mulai terasa lambat)

Karena konten portofolio **jarang berubah** (Profile/Skill/Achievement diedit manual lewat admin, bukan tiap detik), ini kandidat ideal untuk cache:

```python
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

@method_decorator(cache_page(60 * 15), name='dispatch')  # cache 15 menit
class HomeView(ListView):
    ...
```
Untuk serverless (Vercel), gunakan **cache backend eksternal** (bukan `LocMemCache`, karena tiap cold start = memori baru): pakai Redis gratis dari Upstash, atau — lebih sederhana untuk skala ini — cukup andalkan **HTTP cache header + Vercel Edge Cache**:
```python
from django.views.decorators.cache import cache_control

@method_decorator(cache_control(public=True, max_age=900), name='dispatch')
```

## 3. Skalabilitas — kapan perlu dipikirkan lebih lanjut?

Untuk portofolio personal, skala saat ini **tidak butuh** load balancer, read replica, atau CDN kompleks. Yang benar-benar berdampak untuk skala ini justru:

1. **Cold start Vercel** — mitigasi: gunakan `Vercel Cron` untuk *ping* endpoint tiap beberapa menit agar function tetap "hangat" (opsional, hanya jika cold start terasa mengganggu).
2. **Ukuran gambar** — pastikan gambar project/avatar di-resize & di-compress sebelum upload (Cloudinary bisa otomatis transform via URL parameter, mis. `?q_auto,f_auto`).
3. **Database connection limit** — banyak Postgres gratis tier (Neon, Supabase) punya limit koneksi rendah. Karena serverless bisa spawn banyak instance, tambahkan **connection pooling** (Neon & Supabase sudah menyediakan pooler URL — pastikan `DATABASE_URL` pakai endpoint pooler-nya, bukan direct connection).

## 4. Rencana pertumbuhan bertahap (jika portofolio berkembang jadi blog/CMS pribadi)

Jangan bangun ini sekarang — hanya sebagai catatan arah jika suatu saat dibutuhkan:
- Tambah model `BlogPost` dengan editor Markdown (`django-markdownx`) untuk menulis artikel teknis — bagus untuk SEO jangka panjang (lihat `09-seo-strategy.md` §Content Marketing).
- Tambah `sitemap.xml` dinamis via `django.contrib.sitemaps` (sudah dibahas di `09-seo-strategy.md`).
