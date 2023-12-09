from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def erp_scm(request):
    return HttpResponse("Hello Supply Chain Management System")