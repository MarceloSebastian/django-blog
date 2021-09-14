from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts_view, name='posts'),
    path('about/', views.about_view, name='about'),
    path('post/<int:post_id>/', views.post_view, name='post')
]




