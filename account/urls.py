from django.urls import path, include
from . import views
urlpatterns=[
path('', views.home, name="home"),
    path('newsDetail/<int:myid>', views.newsDetail, name='news-Detail'),
    path('about', views.about, name='about'),
path('news', views.news, name='news'),
    path('join us',views.join,name='join-us'),
    path('team', views.team, name='team'),
path('magazine', views.magazine, name='magazine'),
    ]