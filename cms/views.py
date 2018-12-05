from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.http import HttpResponse

def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('前台首页')
    else:
        current_namespace = request.resolver_match.namespace
        print(current_namespace)
        return redirect(reverse("%s:/login"%current_namespace))

def login(request):
    return HttpResponse('CMS登录页')