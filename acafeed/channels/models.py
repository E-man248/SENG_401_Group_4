from django.db import models
from django.utils import timezone
from users.models import User
# Create your models here.

from django.db import models
from django.utils import timezone
from users.models import User

class PostTag(models.Model):
    tagName = models.CharField(max_length=32)

    def __str__(self):
        return str(self.tagName)

class Channel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    date_posted = models.DateTimeField(default=timezone.now)
<<<<<<< Updated upstream
    subscribers = models.ManyToManyField(User)

    def subscribe(self, user):
        self.subscribers.add(user)

    def unsubscribe(self, user):
        u = User.objects.get(userName = user)
        self.topic_set.remove(u)

=======
>>>>>>> Stashed changes

    def __str__(self):
        return str(self.name)

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
    # tags = models.ManyToManyField(PostTag)

    class Meta:
        unique_together = ('title', 'created_by', 'posted_in')
        ordering = ['date_posted']

    def notify(self):
        for subscriber in  self.posted_in.subscribers.all():
            m = Message(messageText = 'New Post in channel: ' + self.posted_in, recipient = subscriber)
            m.save()                
    
    def __str__(self):
        return str(self.title)