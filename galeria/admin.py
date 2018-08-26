from django.contrib import admin
from .models import Category, Media, Clip
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Category)
admin.site.register(Media)
admin.site.register(Clip)
