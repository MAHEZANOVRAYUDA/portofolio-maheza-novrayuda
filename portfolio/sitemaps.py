from django.contrib.sitemaps import Sitemap
from .models import Project

class ProjectSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    
    def items(self):
        return Project.objects.all()
        
    def location(self, obj):
        return f'/projects/{obj.pk}/'

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'
    
    def items(self):
        return ['portfolio:home', 'portfolio:about', 'portfolio:projects', 'portfolio:contact']
        
    def location(self, item):
        from django.urls import reverse
        return reverse(item)
