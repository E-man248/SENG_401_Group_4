from django import forms
from . import models

# Create your forms here.


class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['name', 'email', 'year', 'userName',
                  'password', 'major', 'school']
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['userName', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
