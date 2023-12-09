from django.http import HttpResponse
from django.urls import path 
from . import views
from . serviceViews import  ServiceListView, ServiceDetailView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView
from . customerViews import  CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView




urlpatterns = [
    path('', views.crm_index, name="crm_index"),
    path('services/', ServiceListView.as_view(), name='service_list'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('services/new/', ServiceCreateView.as_view(), name='service_create'),
    path('services/<int:pk>/edit/', ServiceUpdateView.as_view(), name='service_edit'),
    path('services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),

    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/new/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_edit'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
]
