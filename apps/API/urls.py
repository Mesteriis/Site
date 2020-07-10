from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from . import views
from apps.authentication import views as authViews

urlpatterns = [
    # User
    path('', views.description, name='api_description'),
    path('savePSU/', views.savePersonalSettingsUser, name='api_savePSettingsUser'),
]
