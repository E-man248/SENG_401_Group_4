from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


# Create your views here.


def homepage(request):
    return render(request, 'users/home-page.html')


def users_login(request):
    form = LoginForm()
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        if User.objects.filter(userName=userName, password=password).exists():
            user = User.objects.get(userName=userName)
            # This is a session variable and will remain existing as long as you don't delete this manually or clear your browser cache
            request.session['user_id'] = user.id
            return redirect('courses:mycourses')
    return render(request, 'users/login.html', {'form': form})


def users_signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        if User.objects.filter(userName=request.POST['userName']).exists():
            error = "This username is already taken"
            return render(request, 'users/signup.html', {'form': form, 'error': error})
        if User.objects.filter(email=request.POST['email']).exists():
            error = "This email is already taken"
            return render(request, 'users/signup.html', {'form': form, 'error': error})
        form = RegisterForm(request.POST)
        new_user = form.save(commit=False)
        new_user.save()
        return redirect('courses:mycourses')
    return render(request, 'users/signup.html', {'form': form})


def users_logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']  # delete user session
        return redirect('users:login')


def users_myaccount(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'users/user-profile.html', {'user': user})


def users_adminmenu(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'users/admin-menu.html', {'user': user})


def get_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])
