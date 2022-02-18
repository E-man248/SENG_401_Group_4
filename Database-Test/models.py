import here as here
from django.db import models
from django.utils import timezone

class UserTag(models.Model):
    tagName = models.CharField(max_length=32)

class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=100)
    year = models.IntegerField(max_length=2)
    userName = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=16)
    major = models.CharField(max_length=32)
    tag = models.ForeignKey(UserTag, on_delete=models.CASCADE())
    school = models.CharField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)


class Channel(models.Model):
    name = models.CharField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE())


class PostTags(models.Model):
    tagName = models.CharField(max_length=32)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE())
    posted_in = models.ForeignKey(Channel, on_delete=models.CASCADE())

class Course(models.Model):
    name = models.CharField(max_length=255)
    courseCode = models.CharField(max_length=7)
    professor = models.CharField(max_length=255)
    professorEmail = models.CharField(max_length=255)


