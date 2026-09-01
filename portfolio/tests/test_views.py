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
