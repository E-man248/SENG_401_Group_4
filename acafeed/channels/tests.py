from operator import ge
from django.test import TestCase
from django.db import models
from .models import Channel
from .models import Post
from .models import Reply
from .models import Message
from users.models import User
from courses.models import Course


class TestChannelCreation(TestCase):

    def setUp(self):
        Course.objects.create(
            name = "Test Course",
            courseCode = "TEST101",
            sectionNumber = 1,
            faculty = 'Software Engineering',
            professor = 'Some Prof',
            professorEmail = 'someprof@email.com',
            year = 'First Year',
        )

        Channel.objects.create(
            name="Homework",
            course = Course.objects.get(name = "Test Course")
        )

    def test_create_channel(self):
        c = Channel.objects.get(name="Homework")
        self.assertEqual(c.name, "Homework")


class TestPostCreation(TestCase):

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

        Course.objects.create(
            name = "Test Course",
            courseCode = "TEST101",
            sectionNumber = 1,
            faculty = 'Software Engineering',
            professor = 'Some Prof',
            professorEmail = 'someprof@email.com',
            year = 'First Year',
        )

        Channel.objects.create(
            name="test",
            course = Course.objects.get(name = "Test Course")
        )

        Post.objects.create(
            title="Homework",
            content="Hello World!",
            created_by=User.objects.get(userName="New_Guy"),
            posted_in=Channel.objects.get(name="test"),
        ).save()

    def test_create_post(self):
        p = Post.objects.get(title="Homework", )
        self.assertEqual(p.content, "Hello World!")
        self.assertEqual(p.posted_in.name, "test")

class TestReplyCreation(TestCase):
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

        Course.objects.create(
            name = "Test Course",
            courseCode = "TEST101",
            sectionNumber = 1,
            faculty = 'Software Engineering',
            professor = 'Some Prof',
            professorEmail = 'someprof@email.com',
            year = 'First Year',
        )

        Channel.objects.create(
            name="test",
            course = Course.objects.get(name = "Test Course")
        )

        p = Post.objects.create(
            title="Homework",
            content="Hello World!",
            created_by=User.objects.get(userName="New_Guy"),
            posted_in=Channel.objects.get(name="test"),
        )

        Reply.objects.create(
            reply_content = "TEST REPLY",
            created_by = User.objects.get(name="Charles"),
            reply_to = p,
        )

    def test_create_Reply(self):
        c = Channel.objects.get(name = "test")
        p = Post.objects.get(title="Homework", posted_in = c.id)
        r = Reply.objects.get(reply_content = "TEST REPLY", reply_to_id = p.id)
        self.assertEqual(r.reply_content, "TEST REPLY")
        self.assertEqual(r.created_by.name, "Charles")


class TestMessageCreation(TestCase):

    def setUp(self):
        User.objects.create(
            name="Charles",
            email="CharlesHasMail@gmail.com",
            year=3,
            userName="New_Guy",
            password="1234abc",
            major="Software Engineer",
            school="University of Calgary",
        )

        User.objects.create(
            name="Frank",
            email="FrankHasMail@gmail.com",
            year=3,
            userName="Newer_Guy",
            password="1234abc",
            major="Software Engineer",
            school="University of Calgary",
        )

        Course.objects.create(
            name = "Test Course",
            courseCode = "TEST101",
            sectionNumber = 1,
            faculty = 'Software Engineering',
            professor = 'Some Prof',
            professorEmail = 'someprof@email.com',
            year = 'First Year',
        )

        Channel.objects.create(
            name="test",
            course = Course.objects.get(name="Test Course"),
        )
        

        Post.objects.create(
            title="Homework",
            content="Hello World!",
            created_by=User.objects.get(userName="New_Guy"),
            posted_in=Channel.objects.get(name="test")
        )

    def test_message_notify(self):
        p = Post.objects.get(title="Homework")
        c = Channel.objects.get(name="test")
        u = User.objects.get(userName="Newer_Guy")

        c.subscribe(u)
        p.notify()

        messages = u.message_set.filter(messageText = "New post in channel: test for course: Test Course")

        self.assertEqual(messages[0].messageText, "New post in channel: test for course: Test Course")

