from django.test import TestCase
from django.db import models
from models import Channel
from models import Post


# Create your tests here.

class ChannelTestCase(TestCase):

    def setUp(self):

        Channel.objects.create(
            name="Homework",
        )

    def test_create_channel(self):
        c = Channel.objects.get(name="SENG533")
        self.assertEqual(c.name, "SENG533")

class PostTestCase(TestCase):

    def setUp(self):

        Post.objects.create(
            title="Homework",
            content="Hello World!",
            
        )

    def test_create_post(self):
        p = Post.objects.get(name="SENG533")
        self.assertEqual(c.name, "SENG533")
