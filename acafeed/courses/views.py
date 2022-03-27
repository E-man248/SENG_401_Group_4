from django.shortcuts import redirect, render
from users.models import User
from .filter import FindCourseFilter
from .models import Course
from .forms import *

# Create your views here.


def courses_admincreatecourse(request):
    form = AddCourseForm()
    if request.method == 'POST':
        if Course.objects.filter(name=request.POST['name']).exists():
            error = "This course already exists"
            return render(request, 'courses/admin-create-course.html', {'form': form, 'error': error})
        form = AddCourseForm(request.POST)
        new_course = form.save(commit=False)
        new_course.save()
        return redirect('courses:admincreatecourse')

    return render(request, 'courses/admin-create-course.html', {'form': form})


def courses_coursehome(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'courses/course-home.html', {'user': user})
    else:
        return redirect('users:login')


def courses_findcourses(request):
    courses = Course.objects.all()
    myFilter = FindCourseFilter(request.GET, queryset=courses)
    result = myFilter.qs
    return render(request, 'courses/find-courses.html', {'myFilter': myFilter, 'result': result})


def get_user(request):
    return User.objects.get(id=request.session['user_id'])


def courses_mycourses(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'courses/my-courses.html', {'user': user})
    else:
        return redirect('users:login')


def read_message(request):
    readMessages = request.POST.getlist('messages')
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'courses/my-courses.html', {'user': user})
