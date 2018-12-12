# Author:Sunday
from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.login, name='login'),
    path('tem_str/', views.tem_str, name='tem_str'),
]