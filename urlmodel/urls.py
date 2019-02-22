# Author:Sunday
from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    path('extends/', views.extends, name='extends'),
]