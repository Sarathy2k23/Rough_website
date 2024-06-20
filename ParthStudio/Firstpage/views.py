from django.shortcuts import render
from django.http import HttpResponse
import datetime
from Firstpage.models import Student
from . import forms



# Create your views here.
def show(request):
    message="<h1>Hello this is Parth studio</h1>"
    return HttpResponse(message)
def gm(request):
    message="<h1>Good moring welcome to parth studio</h1>"
    return HttpResponse(message)
def ge(request):
    message="<h1>Good evening welcome to parth studio</h1>"
    return HttpResponse(message)
def ga(request):
    message="<h1>Good afternoon welcome to parth studio</h1>"
    return HttpResponse(message)
def display(request):
    mes="Hai"
    date=datetime.datetime.now()
    hour=int(date.strftime('%H'))
    if hour <12:
        mes+=" Good Moring"
        
    else:
        mes+=" good eveng"
        
    time_dict={"real_date":date,"name":name,"greets":mes,"hour":hour}
    return render(request,'Firstpage/demo.html',context=time_dict)

def Db(request):
    data=Student.objects.all()
    Studen_detail={"datas":data}
    return render(request,'Firstpage/demo.html',context=Studen_detail)

def form(request):
    fori=forms.Students_forms()
    form_dict={"form":fori}
    return render(request,'Firstpage/demo.html',context=form_dict)
    
