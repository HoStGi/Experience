from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Загаловок')
    content = models.TextField(blank=True, verbose_name='Комментарий')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время публикации")
    published = models.BooleanField(default=False, verbose_name="Публикация")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"pk": self.pk})   

    def get_delete_event_url(self):
        return reverse("post_delete_url", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
        
class Profile(models.Model):
    addres = models.OneToOneField(User,max_length=250, on_delete=models.CASCADE, verbose_name="Никнейм")
    avatar = models.TextField(max_length=250, null=True, blank=True, unique=True, verbose_name="ссылка на фото")

    def __str__(self):
        return self.addres
