import json

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from . import utils

from apps.authentication.models import Profile, Notification, Task


def checkPermissions(request):
    if not request.user.is_staff:
        return HttpResponse(request, 'Для вас не открыт доступ к внешним API системы')


def description(request):
    checkPermissions(request)
    tamplate_name = 'API/descriptions.html'
    context = {
    }
    return render(request, tamplate_name, context)


def savePersonalSettingsUser(request):
    checkPermissions(request)

    jsObj = json.loads(request.body)

    dashC = {
        'theme': 'white',
        'primeColor': 'purple',
    }

    dashS = {
        'activeModule': {
            'searchPanel': False,
            'corpMessage': False,
        },
        'interfacesStyle': {
            'SizeText': {
                'body': False,
                'navBar': False,
                'sideBar': False,
                'Footer': False,
            },
            'styleSideBar': {
                'flat': False,
                'legacy': False,
                'compact': False,
                'childIndent': False,
            },
            'colorThem': {
                'navBar': '',
                'sidebar': {
                    'Them': 'dark',
                    'color': '',
                },
                'brand': ''
            }
        },
    }
    pack = {

    }

    print(request.body)
    print(request)

    return HttpResponse(request)


@csrf_exempt  # FIXME исправить коректность токена
def sendMail(request):
    jsObj = json.loads(request.body)
    pack = {
        'dep': jsObj['dep'],
        'type': jsObj['type'],
        'title': jsObj['title'],
        'note': jsObj['note'],
        'person': json.loads(jsObj['person']),
        'src': json.loads(jsObj['src']),
        'time': jsObj['time'],
        'isObserv': jsObj['isObserv'],
    }
    # https://docs.djangoproject.com/en/3.0/topics/email/
    send_mail(
        'Беда',
        jsObj['title'] + " - " + jsObj['note'],
        'a.meshcheryakov@omnicomm.pro',
        ['avm@sh-inc.ru'],
        fail_silently=False,
    )
    content = {
        'statusSend': 'ok'
    }
    # print(request)
    return HttpResponse(request, content)


def get_token(request):
    checkPermissions(request)
    if request.GET:
        jsObj = json.loads(request.body)
        res = {
            "error": "",
            "name_token": "",
            "token": ""
        }
        if jsObj['w_token_get'] == 'true':
            try:
                login = User.objects.get(request.user).keyChanters.w_login
                password = User.objects.get(request.user).keyChanters.w_password
            except:
                res['error'] = "Token not received, try again later ..."
                return HttpResponse(request, res)
            try:
                token = utils.getWialonToken(login, password)
            except:
                res['error'] = "Token not received, try again later ..."
                return HttpResponse(request, res)
            return HttpResponse(request, token)
        if jsObj['o_token_get'] == 'true':
            try:
                login = User.objects.get(request.user).keyChanters.o_login
                password = User.objects.get(request.user).keyChanters.o_password
            except:
                res['error'] = "Token not received, try again later ..."
                return HttpResponse(request, res)
            try:
                token = utils.getOmniCommToken(login, password)
            except:
                res['error'] = "Token not received, try again later ..."
                return HttpResponse(request, res)
            return HttpResponse(request, token)
