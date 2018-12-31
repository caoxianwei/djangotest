from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string


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


def tem_str(request):
    # html = render_to_string('index.html')
    # return HttpResponse(html)
    data = {
        'param': 123,
        'id': 2147,
    }
    persons = ['sunday', 'pugi', '张三']
    return render(request, 'index.html', {'person': 'sunday', 'data': data, 'persons': persons})
