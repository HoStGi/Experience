from django.test import SimpleTestCase
from django.urls import path, reverse, resolve
from experience.views import PostCreate, logout_user, post_detail, home, about

class TestUrls(SimpleTestCase):
    
    def test_about_url_is_resolver(self):
        url = reverse('about_url')
        self.assertEqual(resolve(url).func, about)

    def test_home_url_is_resolver(self):
        url = reverse('home_url')
        self.assertEqual(resolve(url).func, home)

    def test_logout_url_is_resolver(self):
        url = reverse('logout_url')
        self.assertEqual(resolve(url).func, logout_user)

    def test_add_post_url_is_resolver(self):
        url = reverse('post_create_url')
        self.assertEqual(resolve(url).func.view_class, PostCreate)
    
    def test_show_post_url_is_resolver(self):
        url = reverse('post_detail_url', args=['1'])
        self.assertEqual(resolve(url).func, post_detail)
    
    