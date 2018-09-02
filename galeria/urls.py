from django.urls import path
from galeria import views

urlpatterns = [
    path('media/<int:id>', views.detail, name='media-detail'),
    path('', views.index, name='media-list'),
    path('search/', views.galerySearch, name='media-search'),
]
