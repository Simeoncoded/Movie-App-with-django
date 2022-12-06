from django.shortcuts import render
from .decorators import *
from .models import *

# Create your views here.
@check
def home(request):
    film=Film.objects.all()
    cartoons = Film.objects.filter(catergory__name='cartoons')
    series=Film.objects.filter(category__name='tvseries')
    movies=Film.objects.filter(category__name='movies')

    kate={'film':film, 'cartoons':cartoons,'movies':movies,'series':series}
    return render(request, 'pages/index.html', context=kate)
def about(request):
    return render(request, 'pages/about.html')
def price(request):
    return render(request, 'pages/pricing.html')
def cata1(request):
    return render(request, 'pages/catalog1.html')
def cata2(request):
    return render(request, 'pages/catalog2.html')
def deta1(request,id):
    film=Film.objects.get(id=id)
    return render(request, 'pages/details1.html',{'film':film})
def deta2(request):
    series=Film.objects.get(id=id)
    episode=Episode.objects.filter(season__film__id=id)
    seasons=Season.objects.filter(film__id=id)
    allseasons=[]
    for season in seasons:
        dic={}
        dic["number"]=season.season_number
        dic["episode"]=season.episode_set.all()
        allseasons.append(dic)
    print(allseasons)
    return render(request, 'pages/details2.html',{'series':series, 'episode':episode,"you":allseasons})
def faq(request):
    return render(request, 'pages/faq.html')