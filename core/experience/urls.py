from django import views


from .views import home
from django.urls import path
from .views import logout_user, about, CreatePost
urlpatterns = [
    path('', about, name='about'),
    path('home/', home, name='home'),
    path('about/', logout_user, name='logout'),
    path('add_post/', CreatePost.as_view(), name='add_post')

]
