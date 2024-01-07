from django.shortcuts import render
from django.http import HttpResponse

## Create views

def forum(request):
    return HttpResponse("Forum")