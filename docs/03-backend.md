# Backend — Perbaikan Model, Form, dan Admin

## 1. Penilaian model eksisting

`portfolio/models.py` sudah dirancang cukup baik: `Profile` sebagai singleton (validasi `clean()` mencegah instance kedua), `Project` dengan slug otomatis, `Achievement`/`Certificate`/`Education` dengan `ordering` manual. Ini pola yang tepat untuk portofolio — **pertahankan struktur ini**, jangan dirombak total.

## 2. Perbaikan yang direkomendasikan

### a. `ContactForm` & anti-spam
Cek `portfolio/forms.py` — pastikan ada:
- **Honeypot field** tersembunyi (field yang harus kosong; bila terisi = bot) — cara termudah tanpa dependency eksternal.
- **Rate limiting** sederhana per-IP untuk endpoint `contact` (pakai `django-ratelimit` atau cache-based counter) supaya tidak dibanjiri form spam.
- Validasi email server-side (Django `EmailField` sudah otomatis, tapi tambahkan pesan error dalam Bahasa Indonesia yang jelas).

### b. Notifikasi contact message
Saat ini `ContactMessage` hanya tersimpan ke DB (`form.save()` di `ContactView.form_valid`). Tambahkan:
```python
from django.core.mail import send_mail

def form_valid(self, form):
    obj = form.save()
    send_mail(
        subject=f"Pesan baru dari {obj.name}",
        message=obj.message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
        fail_silently=True,
    )
    messages.success(self.request, 'Terima kasih! Pesan Anda sudah terkirim.')
    return super().form_valid(form)
```
Gunakan layanan email transaksional gratis untuk tier kecil: **Resend**, **Brevo (Sendinblue)**, atau SMTP Gmail App Password untuk awal. Simpan kredensial via environment variable (`EMAIL_HOST_PASSWORD`, dll), jangan hardcode.

### c. Optimasi query
`HomeView.get_context_data` dan `AboutView.get_context_data` melakukan loop Python manual untuk group skill by category:
```python
skills = Skill.objects.all()
skills_by_category = {}
for skill in skills:
    ...
```
Ini oke untuk skala kecil (puluhan skill), tapi lebih rapi & scalable pakai `itertools.groupby` setelah `order_by('category')`, atau — karena data ini jarang berubah — **cache hasilnya** (lihat `05-system-design.md` §Caching).

Tambahkan `select_related`/`prefetch_related` untuk hindari N+1 query:
```python
# ProjectListView & ProjectDetailView
Project.objects.prefetch_related('skills')
```

### d. Django Admin — perkuat supaya Maheza bisa kelola konten tanpa coding lagi
```python
# portfolio/admin.py
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'created_at')
    list_filter = ('featured', 'skills')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('skills',)
    search_fields = ('title', 'description')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Profile.objects.exists()  # cegah duplikat singleton dari UI admin juga
```

### e. Validasi upload file
`Project.document`, `Certificate.file`, `Skill.icon` menerima upload bebas. Tambahkan validator ekstensi & ukuran file:
```python
from django.core.validators import FileExtensionValidator

file = models.FileField(
    upload_to='certificates/files/',
    validators=[FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png'])],
    blank=True, null=True,
)
```
Batasi ukuran maksimum di level form (Django tidak punya validator ukuran bawaan) — tambahkan `clean_file()` custom di form terkait.

## 3. Testing dasar yang harus ditambahkan

Saat ini tidak terlihat file test. Tambahkan minimal:
- `portfolio/tests/test_models.py` — pastikan `Profile.clean()` menolak instance kedua, slug `Project` unik otomatis
- `portfolio/tests/test_views.py` — pastikan semua halaman return 200, `ContactView` submit valid menyimpan `ContactMessage`

```python
class ProfileSingletonTest(TestCase):
    def test_cannot_create_second_profile(self):
        Profile.objects.create(name="A", hero_title="X", bio="Y")
        with self.assertRaises(ValidationError):
            Profile.objects.create(name="B", hero_title="X", bio="Y")
```

## 4. API (opsional, untuk pengembangan masa depan)
Jika suatu saat ingin frontend terpisah (mis. Next.js) atau integrasi mobile, model sudah rapi untuk diekspos via **Django REST Framework**. Tidak perlu dilakukan sekarang — cukup dicatat sebagai opsi masa depan, jangan over-engineer di tahap ini.
