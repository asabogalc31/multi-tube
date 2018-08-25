from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
'''  
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_names = models.CharField(max_length=100)
    last_names = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique= True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    alias = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    link = models.URLField(max_length=150, null=True, blank=True)
    avatar = models.ImageField(upload_to=upload_to, null=True, blank=True)

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"

    def __str__(self):
        return "@{} {}".format(self.user, self.email)

    def set_in_session(self, request):
        data = {}
        data['alias'] = self.alias
        data['email'] = self.email
        data['description'] = self.description
        data['link'] = self.link
        data['avatar'] = str(self.avatar)
        request.session['profile'] = data

class User
    
    '''