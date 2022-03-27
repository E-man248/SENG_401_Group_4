from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from courses.models import Course
from users.models import User
# Create your models here.

from django.db import models
from django.utils import timezone
from users.models import User


class Channel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    date_posted = models.DateTimeField(default=timezone.now)
    subscribers = models.ManyToManyField(User)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)

    def subscribe(self, user):
        self.subscribers.add(user)

    def unsubscribe(self, user):
        u = User.objects.get(userName=user)
        self.topic_set.remove(u)

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    messageText = models.TextField(max_length=255)
    dateSent = models.DateTimeField(default=timezone.now)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    readFlag = models.BooleanField(default=False)

    def __str__(self):
        return str(self.messageText)

    class Meta:
        ordering = ['-dateSent']


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_in = models.ForeignKey(Channel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('title', 'created_by', 'posted_in')
        ordering = ['date_posted']

    def notify(self):
        for subscriber in self.posted_in.subscribers.all():
            if subscriber.username != self.created_by.username:
                m = Message(messageText='New post in channel: ' + self.posted_in.name, recipient=subscriber)
                m.save()

    def __str__(self):
        return str(self.title)


class Reply(models.Model):
    reply_content = models.TextField(max_length=255)
    reply_date = models.DateField(default=timezone.now)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    reply_to = models.ForeignKey(Post,on_delete=models.CASCADE)

    class Meta:
        ordering = ['reply_date']

    def __str__(self):
        return str(self.reply_content)