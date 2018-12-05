from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def book(request):
    a = 0
    b = 1
    # c = b/a
    return HttpResponse('书籍')


def book_detail(request, book_id, category_id):
    text = '您输入的图书id是：%s, 图书分类是：%s' % (book_id, category_id)
    return HttpResponse(text)

def author_detail(request):
    anthor_id = request.GET.get('id')
    text = '作者的id是：%s' % anthor_id
    return HttpResponse(text)
