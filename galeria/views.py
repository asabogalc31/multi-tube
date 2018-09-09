import smtplib
from django.shortcuts import render
from email.mime.text import MIMEText as text
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
        gmail_user = 'multitube.grupo02@gmail.com'
        to = [media.user.email]
        title_video = media.title
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, "tubegrupo2")
        body = "¡Hola, " + media.user.first_name + "! \n\n El video " + title_video +" que publicaste en mediatube le han agregado un clip puedes ir a verlo. \n\n ¡Saludos Media-Tube!"
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
