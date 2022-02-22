from django.db import models
from django.utils import timezone


# Create your models here.

class UserTag(models.Model):
    tagName = models.CharField(max_length=32)

    def __str__(self):
        return str(self.tagName)


class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=100, unique=True)
    year = models.IntegerField()
    userName = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=16)
    major = models.CharField(max_length=32)
    tag = models.ManyToManyField(UserTag)
    school = models.CharField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.userName)
