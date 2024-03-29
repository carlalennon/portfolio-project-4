from django.shortcuts import render
from django.views import generic
from .models import Thread

## Create views
class ThreadList(generic.ListView):
    queryset = Thread.objects.all()
    template_name = "forum/index.html"
    paginate_by = 6