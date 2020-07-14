import datetime
import json

from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from _Site.settings import BASE_DIR
from . import utils
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

from django.views.decorators.csrf import csrf_exempt

from .forms import UploadFileForm


from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm





# Create your views here.
@login_required(login_url="/login/")
def csa(request):
    online = utils.get_data_online()
    if request.method == 'POST' and request.FILES['1c_data']:
        dataFile1c = request.FILES['1c_data']
        fs = FileSystemStorage()

        print(dataFile1c.name)
        print(dataFile1c)
        filename = fs.save(dataFile1c.name, dataFile1c)
        uploaded_file_url = fs.url(filename)

        req = utils.read_data_1c(BASE_DIR + uploaded_file_url)
        if not req['error_fnc']:
            context = {
                '1c_data_info': req['info'],
                '1c_data': {
                    'other': req['other'],
                    'noID': req['noID'],
                    'block': req['block'],
                    'error': req['error']
                },
                'online': online,
                'date_act': '30.07.2020'
            }
        else:
            context = {
                'error': '1c_analise_error'
            }
            print(context['1c_data_info'])
        return render(request, 'csa/index.html', context)

    context = {
        'online': online
    }
    templates_name = 'csa/index.html'

    return render(request, templates_name, context)


def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')
