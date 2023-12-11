# views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import  Service

class ServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'

class ServiceCreateView(CreateView):
    model = Service
    template_name = 'service_form.html'
    fields = ['name', 'price']
    success_url = reverse_lazy('service_list')

class ServiceUpdateView(UpdateView):
    model = Service
    template_name = 'service_form_update.html'
    fields = ['name', 'price']
    success_url = reverse_lazy('service_list')

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service_confirm_delete.html'
    success_url = reverse_lazy('service_list')

