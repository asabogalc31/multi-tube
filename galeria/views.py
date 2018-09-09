import smtplib
from django.shortcuts import render
from email.mime.text import MIMEText as text
from .models import Media, Clip, Category
from .forms import ClipForm
import requests

# Create your views here.
def index(request):

    port = request.META['SERVER_PORT']
    response = requests.get('http://localhost:'+port+'/api/media.json/')
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

    port = request.META['SERVER_PORT']
    response = requests.get('http://localhost:'+port+'/api/media/'+str(id)+'.json/')
    media = response.json()
    response = requests.get('http://localhost:'+port+'/api/media/'+str(id)+'/clips.json/')
    clips = response.json()

    form = ClipForm(request.POST or None)
    if form.is_valid():
        clip_media = Media.objects.get(id=id)
        Clip.objects.create(**form.cleaned_data, media=clip_media, user=request.user)

        gmail_user = 'multitube.grupo02@gmail.com'
        to = [request.user.email]
        title_video = clip_media.title
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, "tubegrupo2")
        body = "¡Hola, " + request.user.first_name + "! \n\n Al video " + title_video +" publicado en media-tube le has agregado un clip puedes ir a verlo. \n\n ¡Saludos Media-Tube!"
        m = text(body)
        m['Subject'] = '¡Clip adicionado!'
        m['From'] = gmail_user
        m['To'] = to[0]
        server.sendmail(gmail_user, ", ".join(to), m.as_string())
        server.close()
        form = ClipForm()

    context = {
        'item': media,
        'clips': clips,
        'form': form
    }
    return render(request, 'galeria/mediaDetail.html', context)
