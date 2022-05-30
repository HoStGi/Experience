from django.shortcuts import render
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import CreateView
from django import forms


class AddPostForm(forms.Form):
    pass


class CreatePost(CreateView):
    form = AddPostForm
    model = Post
    template_name = 'experience/add_post.html'
    fields = ('title', 'content')
    success_url: reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_invalid(form)




def home(request):
    current_user = request.user
    count = Post.objects.count()
    if count == 0:
        return render(request, 'experience/home.html', {'count':count})
    else:
        posts = Post.objects.filter(author=current_user)
        return render(request, 'experience/home.html', {'posts': posts, 'count':count})
    
def about(request):
    return render(request, 'experience/about.html')

def logout_user(request):
    logout(request)
    return render(request, 'experience/about.html')