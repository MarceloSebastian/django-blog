from django.shortcuts import render, redirect
from .models import Post
from .forms import CreateForm, CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

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

@login_required
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

@login_required
def edit_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = CreateForm(instance=post)

    context = {'form': form}
    return render(request, 'blog/edit_view.html', context)


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts')

def register_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('home')
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'blog/register_view.html', context)


