from django.shortcuts import render, redirect
from .models import Post
from .forms import CreateForm

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

def create_view(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = request.user
            post.save()
            return redirect('posts')
    else:
        form = CreateForm()

    context = {'form': form}
    return render(request, 'blog/create_view.html', context)

