from django.test import TestCase
from django.core.exceptions import ValidationError
from portfolio.models import Profile, Project
from datetime import date

class ProfileSingletonTest(TestCase):
    def test_cannot_create_second_profile(self):
        Profile.objects.create(name="A", hero_title="X", bio="Y")
        with self.assertRaises(ValidationError):
            p2 = Profile(name="B", hero_title="X", bio="Y")
            p2.full_clean()
            p2.save()

class ProjectSlugTest(TestCase):
    def test_slug_auto_generation(self):
        p1 = Project.objects.create(title="My Project", description="Test", created_at=date.today())
        self.assertEqual(p1.slug, "my-project")
        
        # Test unique slug
        p2 = Project.objects.create(title="My Project", description="Test 2", created_at=date.today())
        self.assertEqual(p2.slug, "my-project-1")
