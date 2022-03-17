from django.db import models
from django.utils import timezone
from users.models import User
from eventsourcing.application import Application
from eventsourcing.domain import Aggregate, event
from uuid import uuid5, NAMESPACE_URL, UUID


# Create your models here.


class Channel(Aggregate):
    # name = models.CharField(max_length=255, unique=True)
    # date_posted = models.DateTimeField(default=timezone.now)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    @event('RegisteredChannel')
    def __init__(self, name: str, user: User):
        self.name = name
        self.date_posted = timezone.now()
        self.created_by = user

    @staticmethod
    def create_id(name):
        return uuid5(NAMESPACE_URL, f'/channels/{name}')

    def __str__(self):
        return str(self.title)


class ChannelApp(Application):
    def register(self, name, user):
        channel = Channel(name, user)
        self.save(channel)

    def edit(self, channel_id: UUID, updated_title: str):
        channel = self.repository.get(channel_id)
        channel.title = updated_title
        self.save(channel)

    def get_channel(self, channel_id: UUID) -> Channel:
        aggregate = self.repository.get(channel_id)
        assert isinstance(aggregate, Channel)
        return aggregate


# class Channel(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     date_posted = models.DateTimeField(default=timezone.now)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.name)


class PostTag(models.Model):
    tagName = models.CharField(max_length=32)

    def __str__(self):
        return str(self.tagName)


class Post(Aggregate):
    # title = models.CharField(max_length=255)
    # content = models.TextField()
    # date_posted = models.DateTimeField(default=timezone.now)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # posted_in = models.ForeignKey(Channel, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(PostTag)

    @event('Posted')
    def __init__(self, title: str, content: str, channel: Channel, user: User, tags: PostTag):
        self.title = title
        self.content = content
        self.date_posted = models.DateTimeField(default=timezone.now)
        self.created_by = models.ForeignKey(user, on_delete=models.CASCADE)
        self.posted_in = models.ForeignKey(channel, on_delete=models.CASCADE)
        self.tags = models.ManyToManyField(tags)
        
    @event('Edited')
    def editContent(self, correction: str):
        self.content = correction

    def __str__(self):
        return str(self.title)

    @staticmethod
    def create_id(title):
        return uuid5(NAMESPACE_URL, f'/posts/{title}')


class PostApp(Application):
    def register(self, title: str, content: str, channel: Channel, user: User, tags: PostTag):
        post = Post(title, content, channel, user, tags)
        self.save(post)

    def edit(self, post: Post, updated_content: str):
        post.content = updated_content
        self.save(post)

    def get_post(self, post_id: UUID) -> Post:
        aggregate = self.repository.get(post_id)
        assert isinstance(aggregate, Post)
        return aggregate


# class Post(models.Model):
#     class Meta:
#         unique_together = ('title', 'created_by', 'posted_in')
#
#     def __str__(self):
#         return str(self.title)
