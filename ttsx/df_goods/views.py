from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *


def index(request):
    typelist = TypeInfo.objects.all().order_by('-id')
    type0 = typelist[0].goodinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodinfo_set.order_by('gclick')[0:4]
    type1 = typelist[0].goodinfo_set.order_by('-id')[0:4]
    type11 = typelist[0].goodinfo_set.order_by('gclick')[0:4]
    type2 = typelist[0].goodinfo_set.order_by('-id')[0:4]
    type21 = typelist[0].goodinfo_set.order_by('gclick')[0:4]
    type3 = typelist[0].goodinfo_set.order_by('-id')[0:4]
    type31 = typelist[0].goodinfo_set.order_by('gclick')[0:4]
    type4 = typelist[0].goodinfo_set.order_by('-id')[0:4]
    type41 = typelist[0].goodinfo_set.order_by('gclick')[0:4]
    type5 = typelist[0].goodinfo_set.order_by('-id')[0:4]
    type51 = typelist[0].goodinfo_set.order_by('gclick')[0:4]
    context={'typelist':typelist,
            'type0':type0,'type01':type01,
             'type1': type1, 'type11': type11,
             'type2': type2, 'type21': type21,
             'type3': type3, 'type31': type31,
             'type4': type4, 'type41': type41,
             'type5': type5, 'type51': type51,}
    return render(request,'df_goods/index.html',context)


def list(request,mod,index,sort):
    typeinfo = TypeInfo.objects.get(pk=mod)
    news = typeinfo.goodinfo_set.order_by('-id')[0:2]
    if sort == 1 :
        goodslist = GoodInfo.objects.filter(gtype_id=int(mod)).order_by('-id')
    elif sort == 2:
        goodslist = GoodInfo.objects.filter(gtype_id = int(mod)).order_by('-gprice')
    elif sort == 3:
        goodslist = GoodInfo.objects.filter(gtype_id=int(mod)).order_by('-gclick')

    paginator = Paginator(goodslist,10)
    page = paginator.page(int(index))

    context={'page':page,
             'paginator':paginator,
             'typeinfo':typeinfo,
             'sort':sort,
             'news':news}
    return render(request,'df_goods/list.html',context)


def detail(request,id):
    good = GoodInfo.objects.get(pk=id)
    good.gclick = good.gclick+1
    good.save()
    news = good.gtype.goodinfo_set.order_by('-id')[0:2]

    context = {'title':good.gtype.ttitle,
               'g':good,
               'news':news,
               'id':id}
    response = render(request,'df_goods/detail.html',context)

    good_ids = request.COOKIES.get('good_ids','')
    good_id = '%d'%good.id
    if good_ids!= '':
        good_ids1 = good_ids.split(',')
        if good_ids1.count(good_id)>=1:
            good_ids1.remove(good_id)
        good_ids1.insert(0,good_id)
        if len(good_ids1)>=6:
            del good_ids1[5]
        good_ids= ','.join(good_ids1)
    else:
        good_ids = good_id
    response.set_cookie('good_ids',good_ids)

    return response