from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from galeria.models import Media
from .serializers import MediaSerializer

@csrf_exempt
def media_list(request):

    if request.method == 'GET':
        media = Media.objects.all()
        serializer = MediaSerializer(media, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def media_detail(request, pk):

    try:
        media = Media.objects.get(pk=pk)
    except Media.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MediaSerializer(media)
        return JsonResponse(serializer.data)
