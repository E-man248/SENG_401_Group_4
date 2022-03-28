from django import forms
from . import models

# Create your forms here.


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = models.Reply
        fields = ['reply_content']


class AddChannelForm(forms.ModelForm):
    class Meta:
        model = models.Channel
        fields = ['name', 'course']


class DeleteChannelForm(forms.ModelForm):
    class Meta:
        model = models.Channel
        fields = ['name']