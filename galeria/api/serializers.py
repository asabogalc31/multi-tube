from rest_framework import serializers
from galeria.models import Media, Clip

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            'title',
            'author',
            'date',
            'city',
            'country',
            'category',
            'type',
            'url',
        )

class ClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clip
        fields = (
            'name',
            'start',
            'end',
            'user',
            'media',
        )
