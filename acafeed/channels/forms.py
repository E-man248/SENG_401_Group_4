from django import forms
from . import models

# Create your forms here.


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content']