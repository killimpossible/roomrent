#-*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import *
from user_manage.models import *
from room_manage.models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime
import md5

def to_reg(request):
    section = '欢迎注册为本系统的合法用户'
    return render_to_response('user_manage/to_reg.html',{'section':section})
def reg(request):
        username = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        phone = request.POST['phone']
        contact = request.POST['contact']
        #获取当前时间
        nowtime = datetime.datetime.now()

        try:
            user = User.objects.get(username=username)
            msg = '此用户名已经被注册，请选用其他的用户名'
            return HttpResponse('<script>alert(\'' + msg + '\');history.go(-1)</script>')
        except:
            pass

        if password != re_password:
            msg = '您两次输入的密码不一致，请重使用另外一个！'
            return HttpResponse('<script>alert(\'' + msg + '\');history.go(-1)</script>')
        else:
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.is_staff = 0
                user.is_active = 1
                user.save()
                user_contact = User_contact()
                user_contact.user_id = user.id
                user_contact.phone = phone
                user_contact.contact = contact
                user_contact.save()
                msg = '注册成功，请登陆后使用系统提供的各项功能！'
                return HttpResponse('<script>alert(\'' + msg + '\');window.location.href="/"</script>')
            except:
                msg = '注册失败，请重新尝试！'
                return HttpResponse('<script>alert(\'' + msg + '\');history.go(-1)</script>')
def login(request):
    username = request.POST['user_name']
    password = request.POST['password']
    user = auth.authenticate(username = username,password = password)
    if user is not None and user.is_active == 1:
        auth.login(request, user)
        return HttpResponse("<script>alert('登陆成功!');window.location.href='/user/user_center/';</script>")
    else:
        return HttpResponse("<script>alert('登陆失败，请重新登陆!');history.go(-1);</script>")
def logout(request):
    auth.logout(request)
    return HttpResponse("<script>alert('欢迎再次使用本系统!');window.location.href='/';</script>")


    
@login_required
def user_center(request):
    section = '用户中心'
    user = request.user
    user_id = user.id
    user_name = User.objects.get(id = user_id).username
    room_pubs = Room.objects.filter(pub_man = user).order_by('-pub_date')
    all_room_pubs = Room.objects.all()
    return render_to_response('user_manage/user_center.html',{'section':section,'user_name':user_name,'room_pubs':room_pubs,'all_room_pubs':all_room_pubs})

@login_required
def to_mod_pass(request):
    return render_to_response('user_manage/mod_pass.html')

@login_required
def mod_pass(request):
    user = request.user
    old_password = request.POST['old_password']
    new_password = request.POST['new_password']
    re_new_passowrd = request.POST['re_new_password']

    if not user.check_password(old_password):
        return HttpResponse("<script>alert('原始密码不正确');history.go(-1);</script>")
    if new_password != re_new_passowrd:
        return HttpResponse("<script>alert('两次输入的密码不一致');history.go(-1);</script>")
    user.set_password(new_password)
    user.save()
    return HttpResponse("<script>alert('更新密码成功!');window.location.href='/';</script>")


@login_required
def to_mod_contact(request):
    user = request.user
    try:
        user_contact = User_contact.objects.get(user=user)
    except:
        user_contact = User_contact(user=user)
        user_contact.save()
    return render_to_response('user_manage/mod_contact.html',{'user_contact':user_contact})


@login_required
def mod_contact(request):
    user = request.user
    phone = request.POST['phone']
    contact = request.POST['contact']
    user_contact = User_contact.objects.get(user=user)
    user_contact.phone = phone
    user_contact.contact = contact
    user_contact.save()
    return HttpResponse("<script>alert('修改联系方式成功!');window.location.href='/user/user_center/';</script>")

@login_required
def to_sendmail(request):
    return render_to_response('user_manage/to_sendmail.html')


from smtplib import SMTP
import settings
import string

@login_required
def sendmail(request):
    user = request.user
    title = request.POST['title']
    content = request.POST['content']

    mc = MailCreator()
    header = {'from':'Visitors','to':'PanFei','subject':'%s:from user %s'%(title,user.username)}
    data = [content.encode('utf-8'),'']
    mail = mc.create(header,data)
    try:
        mail_handle = SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
        mail_handle.ehlo()
        mail_handle.starttls()
        mail_handle.ehlo()
        mail_handle.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        mail_handle.sendmail('','wushipeng520@163.com',mail)
        mail_handle.close()
    except:
        return HttpResponse("<script>alert('发送邮件失败!');window.location.href='/user/to_sendmail/';</script>")
    
    return HttpResponse("<script>alert('发送邮件成功!');window.location.href='/user/user_center/';</script>")
