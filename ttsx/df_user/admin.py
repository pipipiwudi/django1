from django.contrib import admin
from .models import *

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['uname','upwda', 'uemail', 'ushou','uaddress','uyoubian','uphone']
    list_per_page = 15


admin.site.register(UserInfo,UserInfoAdmin)