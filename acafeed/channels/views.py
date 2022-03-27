from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User, Post, Channel
from .forms import *
from . import models
from django.utils import timezone
from django.db import models

# Create your views here.


def channels_admincreatechannel(request):
    form = AddChannelForm()
    if request.method == 'POST':
        if Channel.objects.filter(name=request.POST['name']).exists():
            error = "This channel already exists"
            return render(request, 'channels/admin-create-channel.html', {'form': form, 'error': error})
        form = AddChannelForm(request.POST)
        new_channel = form.save(commit=False)
        new_channel.save()
        return redirect('channels:admincreatechannel')
    return render(request, 'channels/admin-create-channel.html', {'form': form})


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


def channels_createreply(request):
    if 'user_id' in request.session:
        user = get_user(request)
        post_id = request.GET.get('post_id')
        form = ReplyForm()

        if request.method == 'GET':
            request.session['last_page'] = request.META.get('HTTP_REFERER', '/')

        if request.method == 'POST':
            form = ReplyForm(request.POST)
            new_reply = form.save(commit=False)
            new_reply.date_posted = timezone.now()
            new_reply.created_by = user
            new_reply.reply_to = Post.objects.get(id=post_id).created_by
            new_reply.save()
            return HttpResponseRedirect(request.session['last_page'])
        return render(request, 'channels/post-home.html', {'form': form, 'user': user})
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