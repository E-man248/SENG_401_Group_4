from django.contrib import admin
from .models import Channel, PostApp, ChannelApp
from .models import Post
from .models import PostTag


# Register your models here.
admin.site.register(Channel)
admin.site.register(Post)
admin.site.register(PostTag)
admin.site.register(PostApp)
admin.site.register(ChannelApp)
# Register your models here.
