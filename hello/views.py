from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def brian(request):
    return HttpResponse('Hello, Brian!')

def david(request):
    return HttpResponse('Hello, David')