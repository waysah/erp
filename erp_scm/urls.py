from django.http import HttpResponse
from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.erp_scm, name="erp_scm")
]