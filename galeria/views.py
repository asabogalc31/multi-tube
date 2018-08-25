from django.shortcuts import render
from .models import Media, Clip

# Create your views here.
def index(request):

    media = Media.objects.all()[:12]

    context = {
        'media': media
    }
    return render(request, 'galeria/mediaList.html', context)

def detail(request):

    media = None

    context = {
        'media': media
    }
    return render(request, 'galeria/mediaDetail.html', context)
