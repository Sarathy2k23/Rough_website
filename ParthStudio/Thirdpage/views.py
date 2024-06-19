from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def Services_views(request):
    time=datetime.datetime.now()
    return HttpResponse('<h1> this is service provider page time is'+str(time)+'</h1>')
