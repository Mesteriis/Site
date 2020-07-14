from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.csa, name='csa'),
    path('send_1c_to_server/', views.upload_file, name='send_1c_to_server'),
]