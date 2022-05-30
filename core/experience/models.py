from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Комментарий")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время публикации")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title