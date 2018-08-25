from django.urls import path
from galeria import views

urlpatterns = [
    path('', views.index, name='index'),
    path('media/', views.detail, name='detail')
]
