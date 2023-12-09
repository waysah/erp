from django.http import HttpResponse
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.crm_index, name="crm_index")
]