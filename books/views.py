from django.shortcuts import render, reverse

# Create your views here.

from django.http import HttpResponse

def books(request):
    # username = request.GET.get('username')
    # if username:
    #     return HttpResponse('shujijjjj书籍')
    # else:
    #     publisher_url = reverse('publisher', kwargs={'publisher_id': 1, 'detail':1})
    #     # publisher_url = reverse('publisher', kwargs={'publisher_id': 1, 'detail':1})+'?name=xx'
    #     return HttpResponse(publisher_url)
    return HttpResponse('shujijjjj书籍')

def book_detail(request, book_id, category_id):
    text = '您输入的图书id是：%s, 图书分类是：%s' % (book_id, category_id)
    return HttpResponse(text)

def author_detail(request):
    anthor_id = request.GET.get('id')
    text = '作者的id是：%s' % anthor_id
    return HttpResponse(text)

def publisher_detail(request,publisher_id):
    text = '出版设为： %s' % publisher_id
    return HttpResponse(text)