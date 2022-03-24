from django.shortcuts import redirect, render
from users.models import User

# Create your views here.


def courses_admincreatecourse(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'courses/admin-create-course.html', {'user': user})


def courses_coursehome(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'courses/course-home.html', {'user': user})


def courses_findcourses(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'courses/find-courses.html', {'user': user})


def get_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])


def courses_mycourses(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'courses/my-courses.html', {'user': user})
    else:
        return redirect('users:login')
