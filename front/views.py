from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.http import HttpResponse

def index(request):
    # ?username = xxx
    username = request.GET.get('username')
    if username:
        return HttpResponse('前台首页')
    else:
        # login_url = reverse("login")
        login_url = reverse("front:login")
        # return redirect('front/signin/')
        return redirect(login_url)

def login(request):
    return HttpResponse('前台登录页')