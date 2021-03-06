from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
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
        if not posts:
            count = 0 
            print(count)
            return render(request, 'experience/home.html', {'count': count})
        return render(request, 'experience/home.html', {'posts': posts, 'count': count})

class PostCreate(CreateView):

    model = Post
    template_name = 'experience/post_create.html'
    fields = ('title', 'content','published',)
    success_url = reverse_lazy('home_url')

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


def post_detail(request, pk):
    current_user = request.user
    post = get_object_or_404(Post, pk=pk, author=current_user)
    if request.method == 'GET':
        return render(request, 'experience/post_detail.html', {"post": post})

    

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        post.delete()
        return redirect('home_url')
