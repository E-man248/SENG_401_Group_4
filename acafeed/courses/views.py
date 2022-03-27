from django.shortcuts import redirect, render
from users.models import User
from .filter import FindCourseFilter
from .models import Course
from .forms import *

# Create your views here.


def courses_admincreatecourse(request):
    if 'user_id' in request.session:
        user = get_user(request)
        form = AddCourseForm()
        if request.method == 'POST':
            if Course.objects.filter(name=request.POST['name']).exists():
                error = "This course already exists"
                return render(request, 'courses/admin-create-course.html', {'form': form, 'error': error, 'user': user})
            form = AddCourseForm(request.POST)
            new_course = form.save(commit=False)
            new_course.save()
            return redirect('courses:admincreatecourse')

        return render(request, 'courses/admin-create-course.html', {'form': form, 'user': user})
    else:
        return redirect('users:login')


def courses_coursehome(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'courses/course-home.html', {'user': user})
    else:
        return redirect('users:login')


def courses_findcourses(request):
    form = AddToMyCoursesForm()
    if 'user_id' in request.session:
        user = get_user(request)
        courses = Course.objects.all()
        myFilter = FindCourseFilter(request.GET, queryset=courses)
        searchresult = myFilter.qs
        checked = user.courses.all()
        checkedresultset = []
        uncheckedresultset = []
        for r in searchresult:
            for c in checked:
                if r == c:
                    checkedresultset.append(r)

        for r in searchresult:
            if r not in checkedresultset:
                uncheckedresultset.append(r)

        if request.method == 'POST':
            user.courses.add(Course.objects.get(name=request.POST['name']))
            user.save()
            return redirect('courses:findcourses')
        return render(request, 'courses/find-courses.html', {'form': form, 'user': user, 'myFilter': myFilter,
                                                             'checked': checkedresultset,
                                                             'unchecked': uncheckedresultset})
    else:
        return redirect('users:login')


def get_user(request):
    return User.objects.get(id=request.session['user_id'])


def courses_mycourses(request):
    if 'user_id' in request.session:
        user = get_user(request)

        if request.GET.get('left_course'):
            course_id = request.GET.get('left_course')
            course = Course.objects.get(id=course_id)
            user.courses.remove(course)

        return render(request, 'courses/my-courses.html', {'user': user})
    else:
        return redirect('users:login')


def read_message(request):
    readMessages = request.POST.getlist('messages')
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'courses/my-courses.html', {'user': user})
