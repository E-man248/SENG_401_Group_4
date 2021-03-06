from django.db import models
from django.utils import timezone
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
    courses = models.ManyToManyField(Course, blank=True)
    blocked = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)

    def getAllMessages(self):
        return self.message_set.all()

    def getUnreadMessages(self):
        ms = self.message_set.filter(readFlag=0)
        # self.setAllRead()
        return ms

    def setAllRead(self):
        ms = self.message_set.filter(readFlag=0)
        for m in ms:
            m.readFlag = True
            m.save()

    def __str__(self):
        return str(self.userName)
