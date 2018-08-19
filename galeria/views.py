from django.shortcuts import render
from .models import Media

# Create your views here.
def index(request):

    media = Media.objects.all()[:12]

    context = {
        'media': media
    }
    return render(request, 'galeria/mediaList.html', context)
