from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from galeria.models import Media, Clip
from .serializers import MediaSerializer, ClipSerializer

@api_view(['GET'])
def media_list(request, format=None):

    if request.method == 'GET':
        media = Media.objects.all()
        serializer = MediaSerializer(media, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def media_detail(request, pk, format=None):

    try:
        media = Media.objects.get(pk=pk)
    except Media.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MediaSerializer(media)
        return Response(serializer.data)

@api_view(['GET'])
def clip_list(request, format=None):

    if request.method == 'GET':
        clips = Clip.objects.all()
        serializer = ClipSerializer(clips, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def clip_detail(request, pk, format=None):

    try:
        clip = Clip.objects.get(pk=pk)
    except Clip.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClipSerializer(clip)
        return Response(serializer.data)

@api_view(['GET'])
def media_clips(request, pk, format=None):
    try:
        media = Media.objects.get(pk=pk)
    except Media.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        clips = Clip.objects.filter(media=media.id)
        serializer = ClipSerializer(clips, many=True)
        return Response(serializer.data)
