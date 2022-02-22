from django.contrib import admin
from .models import User
from .models import UserTag


# Register your models here.
admin.site.register(User)
admin.site.register(UserTag)
