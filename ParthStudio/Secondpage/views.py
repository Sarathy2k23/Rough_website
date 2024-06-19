from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def About_view(request):
    return HttpResponse("<h1>This is About page</h1>")