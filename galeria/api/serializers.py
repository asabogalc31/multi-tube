from rest_framework import serializers
from galeria.models import Media, Clip
from django.contrib.auth.models import User
from django.urls import reverse

class MediaSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField('get_absolute_url')
    type_display = serializers.CharField(source='get_type_display')

    class Meta:
        model = Media
        fields = (
            'id',
            'title',
            'author',
            'date',
            'city',
            'country',
            'category',
            'type_display',
            'url',
            'detail_url'
        )

    def get_absolute_url(self, media):
        return reverse("media-detail", kwargs={"id": media.id})

class ClipSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Clip
        fields = (
            'id',
            'name',
            'start',
            'end',
            'username',
            'media',
        )

    def get_username(self, clip):
        return clip.user.username
