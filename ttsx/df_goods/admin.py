from django.contrib import admin
from .models import *


class TpyeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gtitle','gprice','gclick','gkucun','gtype']


admin.site.register(TypeInfo,TpyeInfoAdmin)
admin.site.register(GoodInfo,GoodsInfoAdmin)