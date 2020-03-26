from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def wage_statistics_views(request, name, wage):
    return HttpResponse(name + '的工资是：' + wage + '元/月')
