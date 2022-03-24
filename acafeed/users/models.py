from django.db import models
from django.utils import timezone
from channels.models import *
from courses.models import *


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=100, unique=True)
    year = models.IntegerField()
    userName = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=16)
    major = models.CharField(max_length=32)
    school = models.CharField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)
    courses = models.ManyToManyField(Course, null=True)
    blocked = models.BooleanField(default=False)

    def unsubscribe(self, channel):
        c = Channel.objects.get(channelName = channel)
        self.topic_set.remove(c)

    def getAllMessages(self):
        return self.message_set.all()

    def getUnreadMesages(self):
        ms = self.message_set.get(readFlag = False)
        for m in ms:
            m.readFlag = True
        return ms    
        
    def __str__(self):
        return str(self.userName)
