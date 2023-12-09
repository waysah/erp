from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def api_index(request):
    return HttpResponse("hello api")

