from django.db import models
from django.utils import timezone
from acafeed.auth.models import User


# Create your models here.


class Channel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class PostTag(models.Model):
    tagName = models.CharField(max_length=32)

    def __str__(self):
        return str(self.tagName)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_in = models.ForeignKey(Channel, on_delete=models.CASCADE)
    tag = models.ForeignKey(PostTag, on_delete=models.CASCADE)

    class Meta(models.Model):
        unique_together = ('title', 'created_by', 'posted_in')

    def __str__(self):
        return str(self.title)
