#coding=utf8
from django.shortcuts import render_to_response
from room_manage.models import *
from django.http import *
def index(request):
    section = '欢迎使用本租赁系统'
    rooms = Room.objects.all().order_by('-pub_date')
    return render_to_response('index.html',{'section':section,'rooms':rooms})
def needLogin(request):
    return HttpResponse('<script>alert("您需要登陆才能使用此功能!");location.href="/"</script>')
