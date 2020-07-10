from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .models import db_online
from .forms import UploadFileForm
# from somewhere import handle_uploaded_file






# Create your views here.
@login_required(login_url="/login/")
def csa(request):
    context = {
    }
    templates_name = 'csa/index.html'

    return render(request, templates_name, context)





def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})
