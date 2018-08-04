from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse('<h1>Hello my django</h1>')


def login(request):
    '''
    django 用来打开文件，获取内容，返回给用户，使用特定的函数render
    render 就相当于
        f = open('templates/login.html','r',encoding='utf-8')
        data = f.read()
        f.close()
        return HttpResponse(data)
    :param request:
    :return:
    '''
    # f = open('templates/login.html','r',encoding='utf-8')
    # data = f.read()
    # f.close()
    #
    # return HttpResponse(data)
    return render(request,'login.html')

