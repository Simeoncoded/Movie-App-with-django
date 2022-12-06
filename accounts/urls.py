from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('signin/',signn,name='signin'),
    path('signup/',signp, name='signup'),
    path('logout/',logt,name='logout'),
]