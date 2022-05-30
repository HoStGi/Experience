from django.urls import path
from .views import *


urlpatterns = [
    path('', about, name='about'),
    path('home/', home, name='home'),
    path('about/', logout_user, name='logout'),
    path('add_post/', CreateList.as_view(), name='add_post')
]