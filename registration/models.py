from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles', null=True, blank=True)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    def __str__(self):
        return self.user.username
