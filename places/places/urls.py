from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    re_path(r'^places/$', views.PlaceList, name='place_list'),
    re_path(r'^placecreate/$', csrf_exempt(views.PlaceCreate), name='place_create'),
]
