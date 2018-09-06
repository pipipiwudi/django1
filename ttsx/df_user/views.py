from django.shortcuts import render,redirect
from .models import *
from hashlib import sha1


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