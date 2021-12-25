from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def home(request):
    news = News.objects.all().order_by('-id')
    magazines = E_Magazine.objects.latest('id')
    # print(magazines)
    return render(request,'tech-index.html',{'news':news,'magazines':magazines})

def newsDetail(request,myid):
    all = News.objects.all().order_by('-id')
    news = News.objects.get(id=myid)
    magazines = E_Magazine.objects.latest('id')
    # print(news)
    relatedPost = []
    count = 0
    for i in all:
        if count < 4:
            if(i.Categoary == news.Categoary):
                relatedPost.append(i)
                count += 1
        else:
            break

    # print(relatedPost)
    return render(request, 'tech-single.html',{'news':news,'relatedPost':relatedPost,'magazines':magazines})

def about(request):
    return render(request,'tech-category-02.html')

def news(request):
    news = News.objects.all().order_by('-id')
    magazines = E_Magazine.objects.latest('id')
    return render(request,'News.html',{'news':news,'magazines':magazines})

def join(request):
    join = join_us.objects.all()
    return render(request,'join us.html',{'join':join})

def team(request):
    return render(request,'team.html');

def magazine(request):
    magazines = E_Magazine.objects.all()
    return render(request,'Magazine.html',{'magazines':magazines})