from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from hashlib import sha1
from . import user_decorator
# from  import GoodInfo
from df_goods.models import GoodInfo

from django.db import models


def register(request):
    return render(request,'df_user/register.html')


def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    pwd = post.get('pwd')
    pwd2 = post.get('cpwd')
    uemail = post.get('email')
    if pwd!= pwd2:
        return redirect('/user/register/')
    s1 = sha1()
    pwd = pwd.encode('utf-8')
    s1.update(pwd)
    upwd = s1.hexdigest()
    user = UserInfo()
    user.uname = uname
    user.upwda = upwd
    user.uemail = uemail
    user.save()
    return redirect('/user/login/')


def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)


def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu',0)
    users = UserInfo.objects.filter(uname=uname)
    print(users)
    if len(users) == 1:
        s1 = sha1()
        upwd = upwd.encode('utf-8')
        s1.update(upwd)
        if s1.hexdigest() == users[0].upwda:
            red = HttpResponseRedirect('/user/info/')
            if jizhu!= 0 :
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'error_name': 0, 'error_pwd': 1, 'uname': uname ,'upwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        context = {'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'df_user/login.html',context)


@user_decorator.login
def info(request):
    uname = request.session['user_name']
    uid = request.session['user_id']
    good_ids = request.COOKIES.get('good_ids','')
    good_ids1 = good_ids.split(',')
    good_list =[]
    for good_id in good_ids1:
        good_list.append(GoodInfo.objects.filter(id=int(good_id)))
    # if uid is None:
    #     return redirect('/user/login/')
    users= UserInfo.objects.filter(pk=uid)
    uaddress = users[0].uaddress
    uphone = users[0].uphone
    context={'uname':uname,'uaddress':uaddress,'uphone':uphone,'good_list':good_list}
    return render(request,'df_user/user_center_info.html',context)


@user_decorator.login
def order(request):
    uid = request.session['user_id']
    users = UserInfo.objects.get(pk=uid)
    uname = users.uname
    uaddress = users.uaddress
    uphone = users.uphone
    ushou = users.ushou
    context = {'uname': uname, 'uaddress': uaddress, 'uphone': uphone,'ushou':ushou}
    return render(request,'df_user/user_center_order.html',context)


@user_decorator.login
def site(request):
    uid = request.session['user_id']
    users = UserInfo.objects.get(pk=uid)
    uname = users.uname
    uaddress = users.uaddress
    uphone = users.uphone
    ushou = users.ushou
    uyoubian = users.uyoubian
    context = {'uname': uname, 'uaddress': uaddress, 'uphone': uphone, 'ushou': ushou,'uyoubian':uyoubian}
    return render(request,'df_user/user_center_site.html',context)


@user_decorator.login
def site_handle(request):
    post = request.POST
    uid = request.session['user_id']
    user = UserInfo.objects.get(pk=uid)
    user.ushou = post.get('ushou')
    user.uphone = post.get('uphone')
    user.uaddress = post.get('uaddress')
    user.uyoubian = post.get('uyoubian')
    user.save()
    return redirect('/user/info/site/')


def logout(request):
    request.session.flush()
    return redirect('/goods/')