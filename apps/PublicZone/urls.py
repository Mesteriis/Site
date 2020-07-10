from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('join/', views.joinAs, name='joniAs'),
]
