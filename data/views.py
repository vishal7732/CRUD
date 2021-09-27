from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .forms import StudentRegistration1
from .models import Student

# Create your views here.

#Add data and View data
def home(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = StudentRegistration() # for blank form
    else:
        fm = StudentRegistration() # for blank form
    stud = Student.objects.all()
    form1 = {'form':fm,'stu':stud}
    return render(request, "index.html",form1)

                    #  OR
#Add data and View data
"""
def home(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['Name']
            em = fm.cleaned_data['email']
            rm = fm.cleaned_data['Roll_No']
            reg = Student(Name=nm,email=em,Roll_No=rm)
            fm.save()
    else:
        fm = StudentRegistration()
    form1 = {'form':fm}
    return render(request, "index.html",form1)"""


# To Update all fields
def update(request,id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    form = {'form':fm}
    return render(request, "update.html",form)

# To Update single fields
def single_edit(request,id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration1(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    pi = Student.objects.get(pk=id)
    fm = StudentRegistration(instance=pi)

    form = {'form':fm,'pi':pi}
    return render(request, "single_update.html",form)





# to delete data
def delete_data(request,id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')