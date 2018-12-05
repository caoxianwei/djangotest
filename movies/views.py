from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('shujijjjj电影集')

def detail(request):
    return HttpResponse('电影详情')