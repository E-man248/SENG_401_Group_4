from django.shortcuts import redirect, render
from users.models import User

# Create your views here.


def courses_admincreatecourse(request):
    return render(request, 'courses/admin-create-course.html')


def courses_coursehome(request):
    return render(request, 'courses/course-home.html')


def courses_findcourses(request):
    return render(request, 'courses/find-courses.html')


def get_user(request):
    return User.objects.get(id=request.session['user_id'])


def courses_mycourses(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'courses/my-courses.html', {'user': user})
    else:
        return redirect('users:login')
