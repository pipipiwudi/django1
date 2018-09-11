from . import views
from django.urls import path


urlpatterns = [
    path('register/',views.register),
    path('register_handle/',views.register_handle),
    path('login/',views.login),
    path('login_handle',views.login_handle),
    path('info/',views.info),
    path('info/order/',views.order),
    path('info/site/',views.site),
    path('site_handle/',views.site_handle),
    path('logout/',views.logout)
]
