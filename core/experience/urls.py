from django.urls import path
from .views import about, home, logout_user, post_detail, post_delete, PostCreate


urlpatterns = [
    path('', about, name='about_url'),
    path('home/', home, name='home_url'),
    path('about/', logout_user, name='logout_url'),
    path('post_detail/<int:pk>/', post_detail, name='post_detail_url'),
    path('delete/<int:pk>/', post_delete, name='post_delete_url'),
    path('post_create/', PostCreate.as_view(), name='post_create_url')
]