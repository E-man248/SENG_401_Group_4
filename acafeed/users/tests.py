from django.test import TestCase
from courses.models import Course
from users.models import User


# Create your tests here.

class TestUserCreation(TestCase):

    def setUp(self):
        testCourse = Course(name="test course", )
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

        testCourse2 = Course(name="test course2", )
        User.objects.create(
            name="Dianne",
            email="DianneHasMail@gmail.com",
            year=2,
            userName="New_Girl",
            password="1234abc",
            major="Software Engineer",
            school="University of Calgary",
            blocked=True
        )

    def test_create_user(self):
        u = User.objects.get(userName="New_Girl")
        self.assertEqual(u.password, "1234abc")
        self.assertEqual(u.year, 2)
        self.assertEqual(u.major, "Software Engineer")
        u2 = User.objects.get(userName="New_Guy")
        self.assertEqual(u2.email, "CharlesHasMail@gmail.com")
        self.assertEqual(u2.school, "University of Calgary")
        self.assertEqual(u2.year, 3)
