from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=32)
    courseCode = models.CharField(max_length=4)
    sectionNumber = models.IntegerField()
    faculty = models.CharField(max_length=32)
    professor = models.CharField(max_length=32)
    professorEmail = models.CharField(max_length=32)

    class Meta:
        unique_together = ('courseCode', 'sectionNumber')

    def __str__(self):
        return str(self.name)
