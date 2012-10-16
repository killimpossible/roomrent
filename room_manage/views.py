#coding=utf8
from room_manage.models import *
from user_manage.models import *
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import *
import datetime
@login_required
def to_room_add(request):
    return render_to_response('room_manage/room_add.html')
@login_required
def room_add(request):
    room_topic = request.POST['room_topic']
    room_desc = request.POST['room_desc']
    house_type = request.POST['house_type']
    square = request.POST['square']
    rent = request.POST['rent']
    pay_type = request.POST['pay_type']
    room_city = request.POST['room_city']
    room_address = request.POST['room_address']
    room_type = request.POST['room_type']
    facilities = request.POST['facilities']

    pub_date = datetime.datetime.now()
    pub_man = request.user


    user_name = User.objects.get(id=request.user.id).username
    
    room = Room()
    try:
        room.room_topic = room_topic
        room.room_desc = room_desc
        room.house_type = house_type
        room.square = square
        room.rent = rent
        room.pay_type = pay_type
        room.pub_man = pub_man
        room.pub_date = pub_date
        room.room_city = room_city
        room.room_address = room_address
        room.room_type = room_type
        room.facilities = facilities
        room.save()
    except:
        return HttpResponse("<script>alert('添加失败，请检查输入是否完整、合法!');window.location.href='/room/to_room_add/';</script>")
    return HttpResponse("<script>alert('添加成功!');window.location.href='/user/user_center/';</script>")
  
def room_detail(request):
    room_id = request.GET.get('room_id','')
    room = Room.objects.get(id=room_id)
    user = room.pub_man
    user_contact = User_contact.objects.get(user=user)
    return render_to_response('room_manage/room_detail.html',{'room':room,'user_contact':user_contact})

@login_required
def room_del(request):
    room_id = request.GET.get('room_id','')
    room = Room.objects.get(id=room_id)
    room.delete()
    return HttpResponse("<script>alert('删除成功!');window.location.href='/user/user_center/';</script>")
