from gc import get_objects
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from experience.models import Post, Profile


def about(request):
    return render(request, 'experience/about.html')


def home(request):
    current_user = request.user
    count = Post.objects.count()

    if count == 0:
        return render(request, 'experience/home.html', {'count': count})
    else:
        posts = Post.objects.filter(author=current_user, published=True)
        return render(request, 'experience/home.html', {'posts': posts, 'count': count})


class CreateList(CreateView):
    model = Post
    template_name = 'experience/add_post.html'
    fields = ('title', 'content','published',)
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def logout_user(request):
    Profile.objects.all().delete()
    Post.objects.filter(published=False).delete()
    logout(request)
    return render(request, 'experience/about.html')



def save_profile(backend, response,user=None, *args, **kwargs):
    Profile.objects.create(
        addres=user,
        avatar=response['photo'],
        
    )
    
def show_post(request, post_id):
    post_item = Post.objects.get(pk=post_id)
    return render(request, 'experience/show_post.html', {"post_item": post_item})
