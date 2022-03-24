from django.db import models
from django.utils import timezone
from users.models import User
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

class Topic(models.Model):
    topicName = models.CharField(max_length=255)
    description = models.TextField(max_length=400, blank=True)
    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return str(self.topicName)


class Message(models.Model):
    messageText = models.TextField(max_length=255)
    dateSent = models.DateTimeField(default = timezone.now)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.messageText)



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_in = models.ForeignKey(Channel, on_delete=models.CASCADE)
    topics  = models.ManyToManyField(Topic)

    class Meta:
        unique_together = ('title', 'created_by', 'posted_in')

    def notify(self):
        topics = self.topics.all()
        for topic in  topics:
            subscribers = topic.subscribers.all()
            for subsciber in subscribers:
                m = Message(messageText = 'TEST MESSAGE',recipient = subsciber)
                m.save()
                
    
    def __str__(self):
        return str(self.title)

