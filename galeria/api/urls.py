from django.conf.urls import url
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^media/$', media_list),
    url(r'^media/(?P<pk>[0-9]+)/$', media_detail),
    url(r'^media/(?P<pk>[0-9]+)/clips/$', media_clips),
    url(r'^clips/$', clip_list),
    url(r'^clips/(?P<pk>[0-9]+)/$', clip_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
