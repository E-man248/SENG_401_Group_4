from django.test import TestCase
from django.db import models
from .models import Channel
from .models import Post
from users.models import User


class ChannelTestCase(TestCase):

    def setUp(self):
        Channel.objects.create(
            name="Homework",
        )

    def test_create_channel(self):
        c = Channel.objects.get(name="Homework")
        self.assertEqual(c.name, "Homework")


class PostChannelTestCase(TestCase):

    def setUp(self):
        u = User(
            name="Charles",
            email="CharlesHasMail@gmail.com",
            year=3,
            userName="New_Guy",
            password="1234abc",
            major="Software Engineer",
            school="University of Calgary",
            blocked=False,
        ).save()

        c = Channel(name="test").save()

        Post.objects.create(
            title="Homework",
            content="Hello World!",
            created_by=User.objects.get(name="Charles"),
            posted_in=Channel.objects.get(name="test"),
        ).save()

    def test_create_post(self):
        p = Post.objects.get(title="Homework", )
        self.assertEqual(p.content, "Hello World!")
        self.assertEqual(p.posted_in.name, "test")


class MessageTestCase(TestCase):

    def setUp(self):
        User.objects.create(
            name="Charles",
            email="CharlesHasMail@gmail.com",
            year=3,
            userName="New_Guy",
            password="1234abc",
            major="Software Engineer",
            school="University of Calgary",
            blocked=False,
        )

        Channel.objects.create(name="test")

        Post.objects.create(
            title="Homework",
            content="Hello World!",
            created_by=User.objects.get(name="Charles"),
            posted_in=Channel.objects.get(name="test"),
        )

    def test_message_notify(self):
        p = Post.objects.get(title="Homework")
        c = Channel.objects.get(name="test")
        u = User.objects.get(name="Charles")

        c.subscribe(u)
        p.notify()

        messages = u.message_set.all()

        self.assertEqual(messages.first.messageText, "New post in channel: " + c.name)

