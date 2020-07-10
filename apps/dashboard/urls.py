# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from . import views
from apps.authentication import views as authViews

urlpatterns = [
    # Matches any html file



    # auth
    path('login/', authViews.login_view, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),

    # dashboard
    path('dashC/', views.dashC, name='dashC'),
    path('dashS/', views.dashS, name='dashS'),
    re_path(r'dashboard/^.*\.html', views.pages, name='pages'),
]
