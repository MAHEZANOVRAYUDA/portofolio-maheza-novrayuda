from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django_ratelimit.decorators import ratelimit

from .models import Project, Skill, Profile, Achievement, Certificate, Education, Experience
from .forms import ContactForm


def get_common_portfolio_context(form=None):
    """Helper to get unified portfolio context for single-page experience."""
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    skills_by_category = {}
    for skill in skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)

    all_projects = Project.objects.prefetch_related('skills').all()
    featured_projects = all_projects.filter(featured=True)[:3]
    achievements = Achievement.objects.all()
    featured_achievements = achievements.filter(is_featured=True)[:3]
    certificates = Certificate.objects.all()
    featured_certificates = certificates.filter(is_featured=True)[:3]
    educations = Education.objects.all()
    experiences = Experience.objects.prefetch_related('skills').all().order_by('ordering', '-start_date')
    featured_experiences = experiences.filter(is_featured=True)

    ctx = {
        'profile': profile,
        'skills': skills,
        'skills_by_category': skills_by_category,
        'projects': all_projects,
        'featured_projects': featured_projects,
        'achievements': achievements,
        'featured_achievements': featured_achievements,
        'certificates': certificates,
        'featured_certificates': featured_certificates,
        'educations': educations,
        'experiences': experiences,
        'featured_experiences': featured_experiences,
        'project_count': all_projects.count() or 15,
        'skill_count': skills.count() or 35,
        'achievement_count': achievements.count() or 3,
        'certificate_count': certificates.count() or 5,
        'experience_count': experiences.count() or 8,
    }
    if form is not None:
        ctx['form'] = form
    elif 'form' not in ctx:
        ctx['form'] = ContactForm()
    return ctx


@method_decorator(cache_control(public=True, max_age=3600), name='dispatch')
class HomeView(ListView):
    model = Project
    template_name = 'home.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.prefetch_related('skills').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_common_portfolio_context())
        context['active_page'] = 'home'
        context['target_section'] = 'home'
        return context


@method_decorator(cache_control(public=True, max_age=3600), name='dispatch')
class AboutView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_common_portfolio_context())
        context['active_page'] = 'about'
        context['target_section'] = 'about'
        return context


@method_decorator(cache_control(public=True, max_age=3600), name='dispatch')
class ProjectListView(ListView):
    model = Project
    template_name = 'home.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.prefetch_related('skills').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_common_portfolio_context())
        context['active_page'] = 'projects'
        context['target_section'] = 'projects'
        return context


@method_decorator(ratelimit(key='ip', rate='5/h', block=True), name='post')
class ContactView(FormView):
    template_name = 'home.html'
    form_class = ContactForm
    success_url = reverse_lazy('portfolio:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common = get_common_portfolio_context()
        for key, val in common.items():
            if key not in context:
                context[key] = val
        context['active_page'] = 'contact'
        context['target_section'] = 'contact'
        return context

    def form_valid(self, form):
        from django.core.mail import send_mail
        from django.conf import settings
        from django.http import JsonResponse

        obj = form.save()

        # Di Vercel (Serverless), proses sinkronus
        send_mail(
            subject=f"Pesan baru dari {obj.name}",
            message=obj.message,
            from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'webmaster@localhost'),
            recipient_list=[getattr(settings, 'CONTACT_NOTIFY_EMAIL', 'admin@localhost')],
            fail_silently=True,
        )

        is_ajax = (
            self.request.headers.get('x-requested-with') == 'XMLHttpRequest' or
            'application/json' in self.request.headers.get('accept', '')
        )
        if is_ajax:
            return JsonResponse({
                'success': True,
                'message': 'Terima kasih! Pesan Anda sudah berhasil terkirim. Saya akan segera merespons secepatnya.'
            })

        messages.success(self.request, 'Terima kasih! Pesan Anda sudah berhasil terkirim.')
        return super().form_valid(form)

    def form_invalid(self, form):
        from django.http import JsonResponse

        is_ajax = (
            self.request.headers.get('x-requested-with') == 'XMLHttpRequest' or
            'application/json' in self.request.headers.get('accept', '')
        )
        if is_ajax:
            return JsonResponse({
                'success': False,
                'message': 'Mohon periksa kembali kolom formulir yang belum sesuai.',
                'errors': {k: [str(err) for err in v] for k, v in form.errors.items()}
            }, status=400)

        return super().form_invalid(form)


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

