from django.shortcuts import render

# Create your views here.


def channels_admincreatechannel(request):
    return render(request, 'channels/admin-create-channel.html')


def channels_channelhome(request):
    return render(request, 'channels/channel-home.html')


def channels_createpost(request):
    return render(request, 'channels/create-post.html')


def channels_posthome(request):
    return render(request, 'channels/post-home.html')