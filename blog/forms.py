from django import forms
from .models import Post

class CreateForm(forms.ModelForm):
    # content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control w-100',
    #                             'id': 'contentsBox', 'placeholder': 'What\'s happening?'}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']



