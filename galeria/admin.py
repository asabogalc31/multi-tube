from django.contrib import admin
from .models import Category, User, Media, Clip

# Register your models here.
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Media)
admin.site.register(Clip)
