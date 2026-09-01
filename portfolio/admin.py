from django.contrib import admin

from .models import (
    Profile,
    Skill,
    Project,
    ContactMessage,
    Achievement,
    Certificate,
    Education,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'hero_title', 'email', 'location')
    fieldsets = (
        ('Identitas', {
            'fields': ('name', 'hero_title', 'bio', 'about_long', 'location', 'avatar'),
        }),
        ('Kontak & Sosial', {
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

    def has_add_permission(self, request):
        # Batasi supaya hanya 1 Profile
        if Profile.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'metrics', 'featured')
    search_fields = ('title', 'description', 'metrics')
    list_filter = ('created_at', 'skills', 'featured')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('skills',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'kind', 'date', 'highlight', 'is_featured', 'ordering')
    list_filter = ('kind', 'is_featured')
    search_fields = ('title', 'organization', 'description', 'highlight')
    ordering = ('ordering', '-date')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'issue_date', 'file', 'is_featured', 'ordering')
    list_filter = ('issuer', 'is_featured')
    search_fields = ('name', 'issuer', 'credential_id')
    ordering = ('ordering', '-issue_date')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_date', 'end_date', 'ordering')
    list_filter = ('start_date', 'end_date')
    search_fields = ('institution', 'degree', 'description')
    ordering = ('ordering', '-start_date')

