from django.shortcuts import render

from .models import Media, Clip, Category
from .forms import ClipForm

# Create your views here.
def index(request):

    media = Media.objects.all()[:12]
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
    media = Media.objects.get(id=id)
    clips = Clip.objects.filter(media=media.id)

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
