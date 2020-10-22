from django.shortcuts import render

from .forms import ApplicationForm
from .models import  Registerdb

def applications_create(request):
    if request.method=='GET':
        form = ApplicationForm()
        return render(request, "hire_me/hire_me.html",{'form' : form})
    else:
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        #return redirect('/list')
def applications_list(request):
    context = {'application_list': Registerdb.objects.all()}
    return render(request, 'hire_me/applications_list.html',context)

def applications_delete(request):
    return
