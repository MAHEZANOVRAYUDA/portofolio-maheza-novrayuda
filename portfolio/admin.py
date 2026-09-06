from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Profile,
    Skill,
    Project,
    ContactMessage,
    Achievement,
    Certificate,
    Education,
    Experience,
)

# Custom Admin Site Branding
admin.site.site_header = "Maheza Novrayuda — Portfolio Administration"
admin.site.site_title = "Admin Portofolio"
admin.site.index_title = "Pusat Kontrol & Manajemen Konten"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('avatar_preview', 'name', 'hero_title', 'email', 'location')
    fieldsets = (
        ('Identitas Utama', {
            'fields': ('name', 'hero_title', 'avatar', 'bio', 'about_long', 'location'),
        }),
        ('Kontak & Media Sosial', {
            'fields': (
                'email',
                'phone',
                'github_url',
                'linkedin_url',
                'instagram_url',
                'portfolio_url',
                'resume_link',
            ),
        }),
    )

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" style="width:36px; height:36px; border-radius:50%; object-fit:cover;" />',
                obj.avatar_optimized_url
            )
        return format_html('<span style="color:#94a3b8;">No Avatar</span>')
    avatar_preview.short_description = "Avatar"

    def has_add_permission(self, request):
        if Profile.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'organization',
        'employment_badge',
        'period_display',
        'is_current',
        'is_featured',
        'ordering',
    )
    list_filter = ('employment_type', 'is_current', 'is_featured', 'location_type')
    search_fields = ('title', 'organization', 'description', 'highlights', 'technologies_summary')
    list_editable = ('is_featured', 'ordering')
    filter_horizontal = ('skills',)
    fieldsets = (
        ('Informasi Peran & Institusi', {
            'fields': ('title', 'organization', 'employment_type', 'is_featured', 'ordering'),
        }),
        ('Waktu & Lokasi Kerja', {
            'fields': (
                ('start_date', 'end_date', 'is_current'),
                ('location', 'location_type'),
            ),
        }),
        ('Deskripsi & Pencapaian Kuantitatif', {
            'fields': ('description', 'highlights'),
            'description': 'Tuliskan pencapaian terukur dengan metrik nyata (misal: 450k+ log, 97.86% akurasi).',
        }),
        ('Keahlian & Tautan Pendukung', {
            'fields': ('technologies_summary', 'skills', 'link'),
        }),
    )

    def employment_badge(self, obj):
        colors = {
            'Research & Academic': '#818cf8',
            'Industrial Internship': '#38bdf8',
            'Apprenticeship': '#34d399',
            'Talent Acceleration': '#fbbf24',
            'Organizational Leadership': '#f472b6',
            'Bootcamp & Training': '#a78bfa',
        }
        color = colors.get(obj.employment_type, '#94a3b8')
        return format_html(
            '<span style="background:{}; color:#0f172a; padding:2px 8px; border-radius:9999px; font-weight:600; font-size:11px;">{}</span>',
            color,
            obj.employment_type
        )
    employment_badge.short_description = "Kategori Peran"

    def period_display(self, obj):
        start = obj.start_date.strftime("%b %Y")
        end = "Sekarang" if (obj.is_current or not obj.end_date) else obj.end_date.strftime("%b %Y")
        return f"{start} — {end}"
    period_display.short_description = "Periode"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'icon_preview')
    list_filter = ('category',)
    search_fields = ('name',)

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="width:24px; height:24px; object-fit:contain;" />', obj.icon.url)
        return "-"
    icon_preview.short_description = "Icon"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('cover_preview', 'title', 'created_at', 'metrics', 'featured')
    search_fields = ('title', 'description', 'metrics')
    list_filter = ('created_at', 'skills', 'featured')
    list_editable = ('featured',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('skills',)

    def cover_preview(self, obj):
        url = obj.preview_image_url
        if url:
            return format_html('<img src="{}" style="width:48px; height:28px; border-radius:4px; object-fit:cover;" />', url)
        return "-"
    cover_preview.short_description = "Preview"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'status_badge')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    actions = ['mark_as_read', 'mark_as_unread']

    def status_badge(self, obj):
        if obj.is_read:
            return format_html('<span style="color:#10b981; font-weight:600;">✓ Sudah Dibaca</span>')
        return format_html('<span style="background:#ef4444; color:#fff; padding:2px 6px; border-radius:4px; font-size:10px; font-weight:bold;">BARU</span>')
    status_badge.short_description = "Status"

    @admin.action(description="Tandai pesan terpilih sebagai sudah dibaca")
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description="Tandai pesan terpilih sebagai belum dibaca")
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'kind', 'date', 'highlight', 'is_featured', 'ordering')
    list_filter = ('kind', 'is_featured')
    search_fields = ('title', 'organization', 'description', 'highlight')
    list_editable = ('is_featured', 'ordering')
    ordering = ('ordering', '-date')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'issue_date', 'document_preview', 'is_featured', 'ordering')
    list_filter = ('issuer', 'is_featured')
    search_fields = ('name', 'issuer', 'credential_id')
    list_editable = ('is_featured', 'ordering')
    ordering = ('ordering', '-issue_date')

    def document_preview(self, obj):
        if obj.file:
            return format_html(
                '<a href="{}" target="_blank" style="color:#0284c7; font-weight:bold;">Lihat Berkas ({})</a>',
                obj.file.url,
                "PDF" if obj.is_pdf else "Gambar"
            )
        if obj.credential_url:
            return format_html('<a href="{}" target="_blank" style="color:#0284c7;">Verifikasi Link</a>', obj.credential_url)
        return format_html('<span style="color:#94a3b8;">Tidak Ada Berkas</span>')
    document_preview.short_description = "Dokumen / Kredensial"


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_date', 'end_date', 'ordering')
    list_filter = ('start_date', 'end_date')
    search_fields = ('institution', 'degree', 'description')
    ordering = ('ordering', '-start_date')


