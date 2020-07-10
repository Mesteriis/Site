import json

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.contrib.auth.models import User
from django.conf import settings
from apps.authentication.models import Profile, Notification, Task


@login_required(login_url="/login/")
def dashC(request):
    isEnableChat = 0

    server = settings.CHAT_WS_SERVER_HOST
    port = settings.CHAT_WS_SERVER_PORT
    protocol = settings.CHAT_WS_SERVER_PROTOCOL
    strAddr = protocol + '://' + server + ':' + str(port) + '/'

    SupportUser = User.objects.all().filter(profile__isSupportChat=True).filter(
        profile__isSupportChatOnlineStatus='on')
    # SupportUser = list(User.objects.all().filter(profile__isSupportChat=True))

    if 0 < len(SupportUser):
        isEnableChat = 0

    chat = {"server": settings.CHAT_WS_SERVER_HOST,
            "port": settings.CHAT_WS_SERVER_PORT,
            "protocol": settings.CHAT_WS_SERVER_PROTOCOL,
            "fullAddres": strAddr,
            "isEnableChat": isEnableChat,
            "SupportUser": SupportUser,
            }

    notification = list(Notification.objects.all().filter(user=request.user).filter(isMarkRead=False))
    tasks = list(Task.objects.all().filter(user=request.user).filter(isCompleted=False))
    profile = Profile.objects.get(user=request.user)

    data = {
        "chat": chat,
        "notification": notification,
        "tasks": tasks,
        "profile": profile,
        "SupportUser": SupportUser,
    }

    template_name = "dashC/dashC.html"

    return render(request, template_name, context=data)

@login_required(login_url="/login/")
def dashS(request):
    server = settings.CHAT_WS_SERVER_HOST
    port = settings.CHAT_WS_SERVER_PORT
    protocol = settings.CHAT_WS_SERVER_PROTOCOL
    strAddr = protocol + '://' + server + ':' + str(port) + '/'

    SupportUser = list(User.objects.all().filter(profile__isSupportChat=True))

    chat = {"server": settings.CHAT_WS_SERVER_HOST,
            "port": settings.CHAT_WS_SERVER_PORT,
            "protocol": settings.CHAT_WS_SERVER_PROTOCOL,
            "fullAddres": strAddr,
            "SupportUser": SupportUser,
            }

    notification = list(Notification.objects.all().filter(user=request.user).filter(isMarkRead=False))
    tasks = list(Task.objects.all().filter(user=request.user).filter(isCompleted=False))
    profile = Profile.objects.get(user=request.user)
    jso = profile.personalSettingsSite

    data = {
        "chat": chat,
        "notification": notification,
        "tasks": tasks,
        "profile": profile,
        "SupportUser": SupportUser,
    }
    # if not request.user.is_staff:
    #     return HttpResponse('You not staff OniCommPro')

    template_name = "dashS/index.html"

    return render(request, template_name, context=data)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('dashC/error-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('dashC/error-500.html')
        return HttpResponse(html_template.render(context, request))


def getUserSettings(request):
    res = User
    print(request)
    return HttpResponse(request, res)


def userPage(request):
    context = {}
    # template = 'dashboard/page-user.html'

    return render(request, template, context)
