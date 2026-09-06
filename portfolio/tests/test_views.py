from django.test import TestCase
from django.urls import reverse
from portfolio.models import Profile, ContactMessage

class PortfolioViewsTest(TestCase):
    def setUp(self):
        Profile.objects.create(name="Test User", hero_title="Hero", bio="Bio")

    def test_home_view_status_code(self):
        response = self.client.get(reverse('portfolio:home'))
        self.assertEqual(response.status_code, 200)

    def test_about_view_status_code(self):
        response = self.client.get(reverse('portfolio:about'))
        self.assertEqual(response.status_code, 200)

    def test_projects_view_status_code(self):
        response = self.client.get(reverse('portfolio:projects'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view_status_code(self):
        response = self.client.get(reverse('portfolio:contact'))
        self.assertEqual(response.status_code, 200)

class ContactFormTest(TestCase):
    def test_contact_form_valid(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Hello',
            'message': 'Test message'
        }
        response = self.client.post(reverse('portfolio:contact'), data)
        self.assertEqual(ContactMessage.objects.count(), 1)
        # Should redirect to success url
        self.assertRedirects(response, reverse('portfolio:contact'))

    def test_contact_form_honeypot(self):
        data = {
            'name': 'Spammer',
            'email': 'spam@example.com',
            'subject': 'Spam',
            'message': 'Buy this',
            'website': 'http://spam.com'
        }
        response = self.client.post(reverse('portfolio:contact'), data)
        self.assertEqual(ContactMessage.objects.count(), 0)
        self.assertFormError(response.context['form'], 'website', 'Spam terdeteksi!')

class ExperienceViewIntegrationTest(TestCase):
    def setUp(self):
        from portfolio.models import Experience
        from datetime import date
        Profile.objects.create(name="Maheza Novrayuda", hero_title="Research Assistant", bio="Bio")
        Experience.objects.create(
            title="Research Assistant",
            organization="LPPM UPI YPTK Padang",
            start_date=date(2026, 6, 1),
            is_current=True,
            description="Software Engineering, AI/ML, Computer Vision, IoT"
        )

    def test_home_view_contains_experiences(self):
        response = self.client.get(reverse('portfolio:home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('experiences', response.context)
        self.assertEqual(response.context['experiences'].count(), 1)
        self.assertContains(response, "Research Assistant")
        self.assertContains(response, "LPPM UPI YPTK Padang")

    def test_admin_panel_accessible(self):
        # Unauthenticated user visiting /admin/ should redirect to login (302) or show login form (200)
        response = self.client.get('/admin/')
        self.assertIn(response.status_code, [200, 302])

