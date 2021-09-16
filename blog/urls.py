from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts_view, name='posts'),
    path('about/', views.about_view, name='about'),
    path('post/<int:post_id>/', views.post_view, name='post'),
    path('create/', views.create_view, name='create'),
    path('edit/<int:post_id>/', views.edit_view, name='edit'),
    path('delete/<int:post_id>/', views.delete, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





