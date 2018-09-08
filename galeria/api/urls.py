from django.conf.urls import url
from .views import media_list, media_detail

urlpatterns = [
    url(r'^media/$', media_list),
    url(r'^media/(?P<pk>[0-9]+)/$', media_detail),
]
