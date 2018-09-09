from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("media-detail", kwargs={"id": self.id})


class Clip(models.Model):
    name = models.CharField(max_length=200)
    start = models.IntegerField()
    end = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
