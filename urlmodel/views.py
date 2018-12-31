from django.shortcuts import render

# Create your views here.

def greet():
    return 'hello, world'


def index(request):
    context = {
        'greet': greet
    }
    return render(request, 'urlmodel.html', context=context)