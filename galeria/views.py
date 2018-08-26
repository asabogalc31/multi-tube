from django.shortcuts import render

from .models import Media, Clip
from .forms import ClipForm, RawClipForm

# Create your views here.
def index(request):

    media = Media.objects.all()[:12]

    context = {
        'media': media
    }
    return render(request, 'galeria/mediaList.html', context)

def detail(request, id):
    form = RawClipForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ClipForm()

    media = Media.objects.get(id=id)
    clips = Clip.objects.filter(media=media.id)

    context = {
        'item': media,
        'clips': clips,
        'form': form
    }
    return render(request, 'galeria/mediaDetail.html', context)
