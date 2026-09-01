from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control

from .models import Project, Skill, Profile, Achievement, Certificate, Education
from .forms import ContactForm


@method_decorator(cache_control(public=True, max_age=3600), name='dispatch')
class HomeView(ListView):
    model = Project
    template_name = 'home.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.prefetch_related('skills').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = Profile.objects.first()

        skills = Skill.objects.all()
        skills_by_category = {}
        for skill in skills:
            if skill.category not in skills_by_category:
                skills_by_category[skill.category] = []
            skills_by_category[skill.category].append(skill)

        featured_projects = Project.objects.prefetch_related('skills').filter(featured=True)[:3]
        featured_achievements = Achievement.objects.filter(is_featured=True)[:3]
        featured_certificates = Certificate.objects.filter(is_featured=True)[:3]

        context.update(
            {
                'profile': profile,
                'skills_by_category': skills_by_category,
                'featured_projects': featured_projects,
                'featured_achievements': featured_achievements,
                'featured_certificates': featured_certificates,
                'active_page': 'home',
            }
        )
        return context


@method_decorator(cache_control(public=True, max_age=3600), name='dispatch')
class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()
        skills = Skill.objects.all()
        projects = Project.objects.prefetch_related('skills').all()
        achievements = Achievement.objects.all()
        certificates = Certificate.objects.all()
        educations = Education.objects.all()

        context.update(
            {
                'profile': profile,
                'skills': skills,
                'projects': projects,
                'achievements': achievements,
                'certificates': certificates,
                'educations': educations,
                'active_page': 'about',
                # Quick stats for sidebar
                'project_count': projects.count(),
                'skill_count': skills.count(),
                'achievement_count': achievements.count(),
                'certificate_count': certificates.count(),
            }
        )
        return context


@method_decorator(cache_control(public=True, max_age=3600), name='dispatch')
class ProjectListView(ListView):
    """Dedicated page listing all projects with category filters."""
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'
    
    def get_queryset(self):
        return Project.objects.prefetch_related('skills').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()

        skills = Skill.objects.all()
        skills_by_category = {}
        for skill in skills:
            if skill.category not in skills_by_category:
                skills_by_category[skill.category] = []
            skills_by_category[skill.category].append(skill)

        context.update(
            {
                'profile': profile,
                'skills_by_category': skills_by_category,
                'active_page': 'projects',
            }
        )
        return context


from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

@method_decorator(ratelimit(key='ip', rate='5/h', block=True), name='post')
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('portfolio:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()
        context.update(
            {
                'profile': profile,
                'active_page': 'contact',
            }
        )
        return context

    def form_valid(self, form):
        from django.core.mail import send_mail
        from django.conf import settings
        import threading
        
        obj = form.save()
        
        def send_email_async():
            send_mail(
                subject=f"Pesan baru dari {obj.name}",
                message=obj.message,
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'webmaster@localhost'),
                recipient_list=[getattr(settings, 'CONTACT_NOTIFY_EMAIL', 'admin@localhost')],
                fail_silently=True,
            )
            
        # Jalankan pengiriman email di thread terpisah agar tidak memblokir response HTTP
        email_thread = threading.Thread(target=send_email_async)
        email_thread.start()
        
        messages.success(self.request, 'Terima kasih! Pesan Anda sudah terkirim.')
        return super().form_valid(form)


@method_decorator(cache_control(public=True, max_age=3600), name='dispatch')
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()
        project = self.object

        # Previous / Next project navigation
        all_projects = list(Project.objects.order_by('-created_at').values_list('pk', flat=True))
        try:
            idx = all_projects.index(project.pk)
        except ValueError:
            idx = -1

        prev_project = None
        next_project = None
        if idx > 0:
            prev_project = Project.objects.filter(pk=all_projects[idx - 1]).first()
        if idx < len(all_projects) - 1 and idx >= 0:
            next_project = Project.objects.filter(pk=all_projects[idx + 1]).first()
        context['profile'] = profile
        context['active_page'] = 'projects'
        context['prev_project'] = prev_project
        context['next_project'] = next_project
        return context
