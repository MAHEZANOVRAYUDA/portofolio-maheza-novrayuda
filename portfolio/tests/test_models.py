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

class ExperienceModelTest(TestCase):
    def test_experience_creation_and_properties(self):
        from portfolio.models import Experience
        exp = Experience.objects.create(
            title="Research Assistant",
            organization="LPPM UPI YPTK Padang",
            employment_type=Experience.EmploymentType.RESEARCH,
            location="Padang, Sumatera Barat",
            location_type=Experience.LocationType.ON_SITE,
            start_date=date(2026, 6, 1),
            is_current=True,
            description="Software Engineering, AI/ML, Computer Vision, IoT",
            highlights="Audit 450k+ log\nDeploy YOLOv8 30+ FPS",
            technologies_summary="Python, YOLOv8, IoT, Docker"
        )
        self.assertEqual(str(exp), "Research Assistant - LPPM UPI YPTK Padang")
        self.assertEqual(len(exp.highlights_list), 2)
        self.assertIn("Audit 450k+ log", exp.highlights_list)
        self.assertEqual(exp.formatted_technologies, ["Python", "YOLOv8", "IoT", "Docker"])

class ZeroAISlopTest(TestCase):
    def test_no_astronomi_or_sma_hallucination(self):
        from portfolio.models import Achievement, Education
        # No KSN astronomi should exist
        astronomi_exists = Achievement.objects.filter(title__icontains="astronomi").exists()
        self.assertFalse(astronomi_exists)
        
        # No high school entries in Education
        sma_exists = Education.objects.filter(institution__icontains="SMA").exists()
        self.assertFalse(sma_exists)

