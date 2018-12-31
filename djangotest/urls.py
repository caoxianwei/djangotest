"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, converters, include
from django.http import HttpResponse

from book.views import book
from movie.views import movie
from books import views
from movies import views as movies
from urlmodel import views as urlmodel


def index(request):
    return HttpResponse('豆瓣首页')

# def book(request):
#     return HttpResponse('书籍')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    # path('book/', book),
    path('book/', include('book.urls')),
    path('city/', include('city.urls')),
    path('movie/', movie),
    path('books/', views.books),
    path('books/detail/<book_id>/<category_id>/', views.book_detail),
    path('books/author/', views.author_detail),
    path('books/publisher/<int:publisher_id>/', views.publisher_detail),


    path('front/', include('front.urls')),
    path('cms/', include('cms.urls', namespace='cms')),
    path('cms1/', include('cms.urls', namespace='cms1')),
    path('cms2/', include('cms.urls', 'cms2')),
    path('url/', include('urlmodel.urls', 'urlmodel')),

    path('movies/', include([
        path('', movies.index),
        path('detail', movies.detail),
    ]))
]
