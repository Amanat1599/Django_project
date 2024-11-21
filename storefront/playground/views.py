from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hel(request):
    return render(request,'hellow.html',{'name':'Amanat'})
