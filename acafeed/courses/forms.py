from django import forms
from . import models
from channels.models import *

# Create your forms here.


class MessageReadForm(forms.ModelForm):
    message = forms.BooleanField()
