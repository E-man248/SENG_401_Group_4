from django.db import models

# Create your models here.


class Course(models.Model):
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

    name = models.CharField(max_length=32, unique=True)
    courseCode = models.CharField(max_length=8, unique=True)
    sectionNumber = models.IntegerField()
    faculty = models.CharField(max_length=32, choices=MAJOR)
    professor = models.CharField(max_length=32)
    professorEmail = models.CharField(max_length=32)
    year = models.CharField(max_length=50, choices=YEAR, null=True)

    class Meta:
        unique_together = ('courseCode', 'sectionNumber')

    def __str__(self):
        return str(self.name)
