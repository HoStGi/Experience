from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from experience.models import Post, Profile


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')

    
    def test_home(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'experience/home.html')
