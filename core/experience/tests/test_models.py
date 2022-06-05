from django.test import TestCase
from experience.models import Post, Profile
from django.contrib.auth.models import User
class PostModelTest(TestCase):

    def test_get_absolute_url(self):
        user = User.objects.create(username='John', email='john@mail.com', password='password')
        Post.objects.create(title='Text title', content='Text content', author=user)
        post=Post.objects.get(id=1)
        self.assertEquals(post.get_absolute_url(), '/post_detail/1/')
    
    def test_get_delete_event_url(self):
        user = User.objects.create(username='John', email='john@mail.com', password='password')
        Post.objects.create(title='Text title', content='Text content', author=user)
        post=Post.objects.get(id=1)
        self.assertEquals(post.get_delete_event_url(), '/delete/1/')

    def test_object_name_is_title(self):
        user = User.objects.create(username='John', email='john@mail.com', password='password')
        Post.objects.create(title='Text title', content='Text content', author=user)
        post=Post.objects.get(id=1)
        expected_object_name = post.title
        self.assertEquals(expected_object_name, str(post))

    def test_object_name_is_addres(self):
        user = User.objects.create(username='John', email='john@mail.com', password='password')
        Profile.objects.create(addres=user, avatar='634634625gdfgegfhfgjxxcv')
        profile=Profile.objects.get(id=1)
        except_object_name=profile.addres_id
        self.assertEquals(except_object_name, profile.id)



