from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User, Post, Channel
from .forms import PostForm
from . import models
from django.utils import timezone
from django.db import models

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
        channel_id = request.GET.get('channel_id')

        if request.method == 'GET':
            request.session['last_page'] = request.META.get('HTTP_REFERER', '/')

        form = PostForm()
        if request.method == 'POST':
            if Post.objects.filter(title=request.POST['title']).exists():
                error = "A post already exists with that title!"
                return render(request, 'channels/channel-home.html', {'form': form, 'error': error, 'user': user})
            form = PostForm(request.POST)
            new_post = form.save(commit=False)
            new_post.date_posted = timezone.now()
            new_post.created_by = user
            new_post.posted_in = Channel.objects.get(id=channel_id)
            new_post.save()
            return HttpResponseRedirect(request.session['last_page'])
        return render(request, 'channels/create-post.html', {'form': form, 'user': user})
    else:
        return redirect('users:login')


def channels_posthome(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'channels/post-home.html', {'user': user})
    else:
        return redirect('users:login')

def get_user(request):
    if 'user_id' in request.session:
        return User.objects.get(id=request.session['user_id'])