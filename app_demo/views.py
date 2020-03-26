from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def hello_views(request):
    return HttpResponse('你好，<br/>世界！')


def msg_views(request, name, age, height9):
    return HttpResponse('我叫：' + name + '<br/>我' + age + '岁了' + '<br/>我身高：' + height9 + 'cm')


def show_views(request, name, address):
    return HttpResponse(name + '的家庭住址在：' + address)
