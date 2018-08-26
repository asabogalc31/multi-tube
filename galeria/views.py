from django.shortcuts import render

from .models import Media, Clip
from .forms import ClipForm

# Create your views here.
def index(request):

    media = Media.objects.all()[:12]

    context = {
        'media': media
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
