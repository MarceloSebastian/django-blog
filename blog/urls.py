from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts_view, name='posts'),
    path('about/', views.about_view, name='about'),
    path('post/<int:post_id>/', views.post_view, name='post'),
    path('create/', views.create_view, name='create'),
    path('edit/<int:post_id>/', views.edit_view, name='edit'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('regiter/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




