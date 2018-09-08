from django.shortcuts import render

from .models import Media, Clip, Category
from .forms import ClipForm
import requests

# Create your views here.
def index(request):

    response = requests.get('http://localhost:8000/api/media.json/')
    media = response.json()
    categories = Category.objects.all()

    context = {
        'searchParams': {
            'type': 'B',
            'category': '',
        },
        'media': media,
        'categories': categories
    }
    return render(request, 'galeria/mediaList.html', context)

def galerySearch(request):
    mediaType = request.GET['mediaType']
    category = request.GET['category']

    media = Media.objects.all()
    if (mediaType != 'B'):
        media = media.filter(type=mediaType)
    if (category != '' and int(category) >= 0):
        cat = Category.objects.get(id=int(category))
        media = media.filter(category=cat.id)

    media = media[:12]
    categories = Category.objects.all()
    categoryId = category
    if (categoryId != ''):
        categoryId = int(categoryId)
    context = {
        'searchParams': {
            'type': mediaType,
            'category': categoryId,
        },
        'category': category,
        'media': media,
        'categories': categories
    }
    return render(request, 'galeria/mediaList.html', context)

def detail(request, id):

    response = requests.get('http://localhost:8000/api/media/'+str(id)+'.json/')
    media = response.json()
    response = requests.get('http://localhost:8000/api/media/'+str(id)+'/clips.json/')
    clips = response.json()

    form = ClipForm(request.POST or None)
    if form.is_valid():
        Clip.objects.create(**form.cleaned_data, media=media, user=request.user)
        form = ClipForm()


    context = {
        'item': media,
        'clips': clips,
        'form': form
    }
    return render(request, 'galeria/mediaDetail.html', context)
