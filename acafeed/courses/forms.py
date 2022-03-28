from django import forms
from django.forms import TextInput

from . import models

# Create your forms here.


class MessageReadForm(forms.ModelForm):
    message = forms.BooleanField()


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['name', 'courseCode', 'sectionNumber', 'faculty',
                  'professor', 'professorEmail', 'year']

        
class AddToMyCoursesForm(forms.ModelForm):
    class Meta:
        model = models.Course
        exclude = ['courseCode', 'sectionNumber', 'faculty', 'professor', 'professorEmail', 'year']
        widgets = {
            'courses': TextInput()
        }


class DeleteCourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['name']