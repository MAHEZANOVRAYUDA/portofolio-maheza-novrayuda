# Security — Hardening untuk Production

## 1. Temuan dari `config/settings.py` saat ini

```python
SECRET_KEY = config('SECRET_KEY')          # ✅ baik, dari env var
DEBUG = config('DEBUG', default=False, cast=bool)  # ✅ default aman
ALLOWED_HOSTS = ['*']                        # ⚠️ terlalu longgar untuk production
```

`ALLOWED_HOSTS = ['*']` membuka celah **HTTP Host header attack** (bisa dipakai untuk cache poisoning atau password-reset link palsu jika suatu saat ada fitur auth). Perbaiki:

```python
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='mahezanovrayuda.com,www.mahezanovrayuda.com,*.vercel.app',
    cast=lambda v: [s.strip() for s in v.split(',')],
)
```

## 2. Security headers yang wajib ditambahkan

Django punya banyak setting keamanan built-in yang **belum diaktifkan** di `settings.py`. Tambahkan blok ini khusus untuk `DEBUG=False`:

```python
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_REFERRER_POLICY = 'same-origin'
```

Catatan: `SECURE_PROXY_SSL_HEADER` sudah benar diset untuk Vercel (`HTTP_X_FORWARDED_PROTO`). Bagus, pertahankan.

## 3. Proteksi form Contact dari spam/abuse

- **Honeypot field** (lihat `03-backend.md`) — cara termudah tanpa dependency.
- **Rate limiting**: install `django-ratelimit`, terapkan di `ContactView.post`:
  ```python
  from django_ratelimit.decorators import ratelimit

  @method_decorator(ratelimit(key='ip', rate='5/h', block=True), name='post')
  class ContactView(FormView):
      ...
  ```
- **CSRF**: Django default sudah aktif via middleware — pastikan tidak ada `@csrf_exempt` yang tidak perlu di codebase.

## 4. Proteksi Django Admin

Admin adalah satu-satunya "pintu belakang" aplikasi ini. Perkuat:
- Ganti URL admin dari `/admin/` ke path custom via env var (mengurangi noise bot scanner otomatis):
  ```python
  # config/urls.py
  path(config('ADMIN_URL', default='admin/'), admin.site.urls),
  ```
- Aktifkan **django-axes** atau minimal rate-limit login admin untuk cegah brute force.
- Gunakan password superuser yang kuat & unik (bukan dipakai ulang dari akun lain).
- Aktifkan 2FA untuk akun admin jika memungkinkan (`django-otp`) — opsional tapi direkomendasikan karena admin ini juga menyimpan `ContactMessage` (data pribadi pengunjung: nama, email).

## 5. Perlindungan data pribadi pengunjung (privasi dasar)

`ContactMessage` menyimpan nama & email pengunjung. Karena ini portofolio publik dengan form terbuka:
- Tambahkan halaman **Kebijakan Privasi** singkat (1 paragraf: data apa yang disimpan, untuk apa, tidak dibagikan ke pihak ketiga) — juga baik untuk kepercayaan rekruter.
- Jangan expose isi `ContactMessage` di endpoint publik manapun (pastikan tidak ada API/serializer yang tidak sengaja membocorkannya).

## 6. Dependency & supply chain

`requirements.txt` pakai range terbuka (`Django>=5.0,<6.0` dst.) — baik untuk fleksibilitas, tapi:
- Jalankan `pip list --outdated` secara berkala.
- Aktifkan **Dependabot** (gratis di GitHub) untuk alert otomatis kalau ada CVE di dependency.
- Pin versi exact di `requirements.txt` untuk production (`Django==5.2.x`) supaya deploy selalu reproducible, sambil tetap update manual secara rutin.

## 7. Upload file — validasi tipe & ukuran

Sudah dibahas di `03-backend.md` §2e — ini juga isu keamanan (mencegah upload file executable menyamar sebagai gambar/PDF). Wajib diterapkan sebelum go-live karena form upload (lewat admin, oleh Maheza sendiri) tetap perlu dijaga standarnya.
