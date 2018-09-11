from django.shortcuts import render, redirect
from df_user import user_decorator
from django.http import JsonResponse
from .models import *


@user_decorator.login
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {'carts':carts,
               'page_name':1}
    return render(request,'df_cart/cart.html',context)


@user_decorator.login
def add(request,gid,count):
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)
    carts = CartInfo.objects.filter(user_id=uid,good_id=gid)
    if len(carts)>=1:
        cart = carts[0]
        cart.count = cart.count +count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.good_id = gid
        cart.count = count
    cart.save()

    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=request.session['user_id']).count()
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')