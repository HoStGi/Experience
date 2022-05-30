from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Загаловок')
    content = models.TextField(blank=True, verbose_name='Комментарий')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время публикации")
    published = models.BooleanField(default=False, verbose_name="Публикация")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
