from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'users/home-page.html')


def users_login(request):
    return render(request, 'users/login.html')


def users_signup(request):
    return render(request, 'users/signup.html')
