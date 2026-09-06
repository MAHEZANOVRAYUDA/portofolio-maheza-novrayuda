from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify


from django.core.validators import FileExtensionValidator

class Skill(models.Model):
    class Category(models.TextChoices):
        LANGUAGES = 'Languages', 'Languages'
        FRAMEWORKS = 'Frameworks', 'Frameworks'
        ML_AI = 'ML/AI Tools', 'ML/AI Tools'
        CLOUD_DEVOPS = 'Cloud/DevOps', 'Cloud/DevOps'

    name = models.CharField(max_length=100)
    icon = models.ImageField(
        upload_to='skills/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'svg'])]
    )
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
    )

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f'{self.name} ({self.category})'


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    created_at = models.DateField()
    metrics = models.CharField(
        max_length=100,
        help_text='Contoh: "Accuracy 95%", "F1 0.89", dll.',
        blank=True,
        null=True,
    )
    featured = models.BooleanField(
        default=False,
        help_text='Tandai jika project ini ingin ditampilkan sebagai highlight.',
    )
    skills = models.ManyToManyField(Skill, related_name='projects', blank=True)
    document = models.FileField(
        upload_to='documents/',
        blank=True,
        null=True,
        help_text='Upload PDF atau dokumen terkait project.',
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])]
    )

    @property
    def preview_image_url(self):
        if self.image:
            return self.image.url
        # If no image uploaded, use GitHub OpenGraph repository card
        if self.github_link and 'github.com/' in self.github_link:
            cleaned = self.github_link.split('github.com/')[-1].strip('/').split('/')
            if len(cleaned) >= 2:
                owner, repo = cleaned[0], cleaned[1]
                repo = repo.split('.')[0]
                return f"https://opengraph.githubassets.com/1/{owner}/{repo}"
        return f"https://opengraph.githubassets.com/1/MAHEZANOVRAYUDA/{self.slug or 'project'}"

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Profile(models.Model):
    # Identitas utama
    name = models.CharField(max_length=150)
    hero_title = models.CharField(
        max_length=150,
        help_text='Contoh: "AI Engineer & Data Enthusiast"',
    )
    bio = models.TextField(
        help_text='Ringkasan singkat (3–5 kalimat) tentang diri Anda.',
    )
    about_long = models.TextField(
        blank=True,
        help_text='Versi lebih panjang untuk halaman About (boleh kosong dulu).',
    )
    location = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        help_text='Foto profil / avatar.',
    )

    # Kontak & sosial
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    portfolio_url = models.URLField(
        blank=True,
        help_text='Jika ada personal domain lain.',
    )
    resume_link = models.URLField(blank=True, null=True)

    @property
    def avatar_optimized_url(self):
        if self.avatar:
            url = self.avatar.url
            if 'cloudinary.com' in url and '/upload/' in url:
                # Cloudinary auto face crop, 400x400 sharp retina, auto quality and format
                return url.replace('/upload/', '/upload/c_fill,w_400,h_400,g_face,q_auto,f_auto/')
            return url
        if self.github_url and 'github.com/' in self.github_url:
            username = self.github_url.rstrip('/').split('/')[-1]
            return f"https://github.com/{username}.png?size=400"
        return "https://github.com/MAHEZANOVRAYUDA.png?size=400"

    @property
    def avatar_thumb_url(self):
        if self.avatar:
            url = self.avatar.url
            if 'cloudinary.com' in url and '/upload/' in url:
                return url.replace('/upload/', '/upload/c_fill,w_120,h_120,g_face,q_auto,f_auto/')
            return url
        return self.avatar_optimized_url

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def clean(self):
        # Singleton: hanya boleh 1 instance
        if not self.pk and Profile.objects.exists():
            raise ValidationError('Hanya boleh ada satu Profile.')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.subject or "No subject"}'


class Achievement(models.Model):
    class Kind(models.TextChoices):
        AWARD = 'award', 'Award / Penghargaan'
        COMPETITION = 'competition', 'Kompetisi'
        CERTIFICATION = 'certification', 'Sertifikasi'
        PROJECT = 'project', 'Project Highlight'
        OTHER = 'other', 'Lainnya'

    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, blank=True)
    kind = models.CharField(
        max_length=20,
        choices=Kind.choices,
        default=Kind.OTHER,
    )
    date = models.DateField(blank=True, null=True)
    highlight = models.CharField(
        max_length=200,
        blank=True,
        help_text='Angka/hasil singkat, mis: "Top 1%", "Gold Medal", "Winner".',
    )
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    is_featured = models.BooleanField(
        default=False,
        help_text='Tampilkan sebagai highlight di halaman utama.',
    )
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering', '-date', 'title']

    def __str__(self):
        return self.title


class Certificate(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=200, blank=True)
    credential_url = models.URLField(blank=True)
    file = models.FileField(
        upload_to='certificates/files/',
        blank=True,
        null=True,
        help_text='Upload sertifikat (PDF/JPG/PNG).',
        validators=[FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png'])]
    )
    image = models.ImageField(upload_to='certificates/', blank=True, null=True, help_text='Legacy field. Gunakan "file" untuk upload baru.')
    ordering = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(
        default=False,
        help_text='Tampilkan di highlight sertifikat.',
    )

    class Meta:
        ordering = ['ordering', '-issue_date', 'name']

    def __str__(self):
        return f'{self.name} - {self.issuer}'

    @property
    def is_pdf(self):
        if self.file:
            return self.file.name.lower().endswith('.pdf')
        return False


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, help_text='Contoh: SMA IPA, Sarjana Komputer')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text='Kosongkan jika masih berlangsung.')
    description = models.TextField(blank=True)
    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering', '-start_date']
        verbose_name_plural = 'Education'

    def __str__(self):
        return f'{self.institution} - {self.degree}'

