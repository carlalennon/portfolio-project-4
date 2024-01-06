from django.shortcuts import render
from django.http import HttpResponse

## Create views

def hello_world(request):
    return HttpResponse("Hello World")