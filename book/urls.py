# Author:Sunday

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book),
    path('detail/<book_id>/<category_id>/', views.book_detail),
    path('author/', views.author_detail)
]