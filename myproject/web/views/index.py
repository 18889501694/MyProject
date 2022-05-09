from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('欢迎进入前台大堂点餐端')
