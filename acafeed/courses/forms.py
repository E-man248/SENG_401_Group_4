from django import forms
from . import models

# Create your forms here.


class MessageReadForm(forms.ModelForm):
    message = forms.BooleanField()


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['name', 'courseCode', 'sectionNumber', 'faculty',
                  'professor', 'professorEmail', 'year']