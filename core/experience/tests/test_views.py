from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from experience.views import about, home, post_detail, post_delete
from experience.models import Post

class TestViews(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()

        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
    
        self.post = Post.objects.create(
            title = 'Test title', content = 'Test content', author = self.user,
        )

        self.about = reverse('about_url')
        self.home = reverse('home_url')
        self.post_detail = reverse('post_detail_url', args=['1'])
        self.PostCreate = reverse('post_create_url')
        self.logout_user = reverse('logout_url')
        self.post_delete = reverse('post_delete_url', args=['1'])

    def test_about(self):
        request = self.factory.get(self.about)
        request.user = self.user
        response = about(request)
        self.assertEquals(response.status_code, 200)

    def test_home(self):
        request = self.factory.get(self.home)
        request.user = self.user
        response = home(request)
        self.assertEquals(response.status_code, 200)
    
    
    def test_post_detail(self):
        request = self.factory.get(self.post_detail)
        request.user = self.user
        response = post_detail(request, pk=1)
        self.assertEquals(response.status_code, 200)
    
    def test_post_delete(self):
        request = self.factory.get(self.post_delete)
        request.user = self.user
        request = post_delete(request, pk=1)
        self.assertEquals(Post.objects.count(), 0)
