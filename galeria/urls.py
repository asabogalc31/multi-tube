from django.urls import path
from galeria import views

urlpatterns = [
    path('', views.index, name='media-list'),
    path('media/<int:id>', views.detail, name='media-detail')
]
