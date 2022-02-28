from django.db import models
from django.utils import timezone
from users.models import User
from eventsourcing.application import Application
from eventsourcing.domain import Aggregate, event


# Create your models here.


class Channel(models.Model, Application):
    name = models.CharField(max_length=255, unique=True)
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def registerPost(self, title, content, user, tag):
        post = Post(title, content, user, self, tag)
        self.save(post)
        return post.id

    def get_post(self, post_id):
        post = self.repository.get(post_id)
        return {'title': post.title, 'content': post.content}


class PostTag(models.Model):
    tagName = models.CharField(max_length=32)

    def __str__(self):
        return str(self.tagName)


class Post(models.Model, Aggregate):
    @event('Posted')
    def __init__(self, title, content, user, channel, tag):
        self.title = title
        self.content = content
        self.created_by = User(user)
        self.posted_in = channel
        self.tag = tag

    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_in = models.ForeignKey(Channel, on_delete=models.CASCADE)
    tags = models.ManyToManyField(PostTag)

    class Meta:
        unique_together = ('title', 'created_by', 'posted_in')

    def __str__(self):
        return str(self.title)
