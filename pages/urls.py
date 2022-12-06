from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('home/',home,name='homepage'),
    path('about/',about,name='aboutpage'),
    path('pricing/',price,name='pricingpage'),
    path('catalog1/', cata1, name='catalogpage'),
    path('catalog2/', cata2, name='catalogspage'),
    path('detail1/<id>/', deta1, name='details1'),
    path('detail2/<id>/', deta2, name='details2'),
    path('faq/', faq, name='faqpage'),


]