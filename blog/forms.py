from django import forms
from .models import Post

class PostItemForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tag', 'image')