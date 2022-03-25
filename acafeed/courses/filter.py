from django.db.models import fields
import django_filters
from django_filters.filters import CharFilter
from django_property_filter import PropertyFilterSet
from django.forms.widgets import TextInput
from django.db.models import Q

from .models import *

class FindCourseFilter(PropertyFilterSet):

    search = CharFilter(method='filter_by_all_name_fields',
                        widget=TextInput(attrs={'placeholder': 'Search...'}))
    YEAR = (
        ('First Year', 'First Year'),
        ('Second Year', 'Second Year'),
        ('Third Year', 'Third Year'),
        ('Fourth Year', 'Fourth Year')
    )
    MAJOR = (
        ('Software Engineering', 'Software Engineering'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Chemical Engineering', 'Chemical Engineering'),
        ('Computer Science', 'Computer Science')
    )
    year = django_filters.ChoiceFilter(
        choices=YEAR,
        label='Undergrad Year',
    )
    faculty = django_filters.ChoiceFilter(
        choices=MAJOR,
        label='Major',
    )

    class Meta:
        model = Course
        fields = ['year', 'faculty']

    def filter_by_all_name_fields(self, queryset, name, value):
        return queryset.filter(
            Q(nameicontains=value) | Q(courseCodeicontains=value) | Q(
                sectionNumbericontains=value) | Q(facultyicontains=value) | Q(professor__icontains=value) | Q(professorEmailicontains=value) | Q(yearicontains=value)
        )