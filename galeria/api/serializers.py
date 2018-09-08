from rest_framework import serializers
from galeria.models import Category, Media, Clip

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
