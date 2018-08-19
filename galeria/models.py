from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

class Media(models.Model):
    MEDIA_TYPES = (
        ('A', 'Audio'),
        ('V', 'Video')
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date = models.DateField(default=datetime.now, blank=True)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=MEDIA_TYPES)
    url = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class User(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_names = models.CharField(max_length=200)
    last_names = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

class Clip(models.Model):
    name = models.CharField(max_length=200)
    start = models.IntegerField()
    end = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
