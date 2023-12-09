from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def crm_index(request):
    return HttpResponse("Hello CRM")