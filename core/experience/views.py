from django.contrib.auth import logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from requests import delete
from experience.models import Post, Profile


def about(request):
    return render(request, 'experience/about.html')


def home(request):
    current_user = request.user
    count = Post.objects.count()

    if count == 0:
        return render(request, 'experience/home.html', {'count': count})
    else:
        posts = Post.objects.filter(author=current_user)
        return render(request, 'experience/home.html', {'posts': posts, 'count': count})


class CreateList(CreateView):
    model = Post
    template_name = 'experience/add_post.html'
    fields = ('title', 'content', 'published',)
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def logout_user(request):
    Profile.objects.all().delete()
    logout(request)
    return render(request, 'experience/about.html')

