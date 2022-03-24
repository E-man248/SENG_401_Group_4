from django.db import models
from django.utils import timezone
from users.models import User
# Create your models here.


class Channel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User)

    def subscribe(self, user):
        self.subscribers.add(user)

    def __str__(self):
        return str(self.name)

# class Topic(models.Model):
#     topicName = models.CharField(max_length=255)
#     description = models.TextField(max_length=400, blank=True)
#     subscribers = models.ManyToManyField(User)

#     def __str__(self):
#         return str(self.topicName)


class Message(models.Model):
    messageText = models.TextField(max_length=255)
    dateSent = models.DateTimeField(default = timezone.now)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    readFlag = models.BooleanField(default = False)

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
    # topics  = models.ManyToManyField(Topic)

    class Meta:
        unique_together = ('title', 'created_by', 'posted_in')
        ordering = ['datePosted']

    def notify(self):
        # topics = self.topics.all()
        for subscriber in  self.posted_in.subscribers.all():
            m = Message(messageText = 'New Post in channel: ' + self.posted_in, recipient = subscriber)
            m.save()                
    
    def __str__(self):
        return str(self.title)

