from django.shortcuts import render

# Create your views here.


def courses_admincreatecourse(request):
    return render(request, 'courses/admin-create-course.html')


def courses_coursehome(request):
    return render(request, 'courses/course-home.html')


def courses_findcourses(request):
    return render(request, 'courses/find-courses.html')


def courses_mycourses(request):
    return render(request, 'courses/my-courses.html')