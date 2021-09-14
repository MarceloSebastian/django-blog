from django.shortcuts import render
from .models import Post

def home(request):
    context = {}
    return render(request, 'blog/home.html', context)

def posts_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/posts_view.html', context)

def about_view(request):
    return render(request, 'blog/about_view.html')

def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blog/post_view.html', context)


