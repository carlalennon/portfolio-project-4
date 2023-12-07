from django.shortcuts import render

# Create your views here.
def loginRequest(request):
    return render(request, 'gknit/login.html')