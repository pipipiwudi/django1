from . import views
from django.urls import path


urlpatterns = [
    path('register/',views.register),
    path('register_handle/',views.register_handle)
]
