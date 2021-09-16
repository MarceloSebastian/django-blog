from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

