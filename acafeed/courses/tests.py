from django.test import TestCase
from django.db import models
from courses.models import Course


# Create your tests here.

class CourseTestCase(TestCase):

    def setUp(self):

        Course.objects.create(
            name="BIOL241",
            sectionNumber=1,
            courseCode="241",
            faculty="Science",
            professor="Holt",
            professorEmail="Holt@home.com"
        )

        Course.objects.create(
            name="SENG533",
            sectionNumber=2,
            courseCode="533",
            faculty="Schulich",
            professor="Moshirpour",
            professorEmail="daddy_mosh@ucalgary.ca"
        )

    def test_create_course(self):
        c = Course.objects.get(name="SENG533")
        self.assertEqual(c.sectionNumber, 2)
        self.assertEqual(c.courseCode, "533")
        self.assertEqual(c.professorEmail, "daddy_mosh@ucalgary.ca")
        c2 = Course.objects.get(name="BIOL241")
        self.assertEqual(c2.faculty, "Science")
        self.assertEqual(c2.professor, "Holt")
        self.assertEqual(c2.courseCode, "241")
