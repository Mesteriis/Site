from django.shortcuts import render, Http404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json
from django.core.mail import send_mail

from django.views import generic
from braces.views import LoginRequiredMixin


def index(request):
    # template = 'index.html'
    template = 'PublicZone/index.html'
    content = {

    }
    return render(request, template, content)


def signIn(request):
    template = 'PublicZone/SignIn.html'
    content = {

    }
    return render(request, template, content)


def joinAs(request):
    template = 'editSettings.html'
    content = {

    }
    return render(request, template, content)


