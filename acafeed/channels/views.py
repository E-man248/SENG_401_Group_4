from django.shortcuts import render, redirect
from .models import User

# Create your views here.


def channels_admincreatechannel(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'channels/admin-create-channel.html', {'user': user})


def channels_channelhome(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'channels/channel-home.html', {'user': user})
    else:
        return redirect('users:login')


def channels_createpost(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'channels/create-post.html', {'user': user})


def channels_posthome(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'channels/post-home.html', {'user': user})

def get_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])