from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def city(request):
    return HttpResponse('sthis is city')