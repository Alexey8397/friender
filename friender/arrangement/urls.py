from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('main_page/', main_page,name="main"),
    path('all_friends/', all_friends,name="friends"),
    path('establishments/', place_arrangments,name="establishments"),
]