from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('list/<int:mod>_<int:index>_<int:sort>',views.list),
    path('<int:id>',views.detail)

]