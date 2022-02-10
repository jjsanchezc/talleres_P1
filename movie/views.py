from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'juan jose',"dia":datetime.now()})

def segundapantalla(request):
    return HttpResponse("esta es la segunda pantallaaa")
#pre incubacion 
