from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart),
    path('add_<int:gid>_<int:count>/',views.add)
]