from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from decouple import config
from django.conf.urls.static import static

urlpatterns = [
    path(config('ADMIN_URL', default='admin/'), admin.site.urls),
    path('', include(('portfolio.urls', 'portfolio'), namespace='portfolio')),
]

from django.views.generic.base import RedirectView, TemplateView
from django.contrib.sitemaps.views import sitemap
from portfolio.sitemaps import ProjectSitemap, StaticViewSitemap

urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico', permanent=True)),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', sitemap, {'sitemaps': {'projects': ProjectSitemap, 'static': StaticViewSitemap}}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


