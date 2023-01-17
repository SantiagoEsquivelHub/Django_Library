from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Permission)