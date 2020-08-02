from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if(request.user.is_authenticated):
        return HttpResponse("ja")
    else:
        return HttpResponse("nein")
