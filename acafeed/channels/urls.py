from django.urls import path
from . import views

app_name = 'channels'

urlpatterns = [
    path('admin-create-channel', views.channels_admincreatechannel, name="admincreatechannel"),
    path('channel-home/', views.channels_channelhome, name="channelhome"),
    path('create-post/', views.channels_createpost, name="createpost"),
    path('post-home/', views.channels_posthome, name="posthome"),
]
