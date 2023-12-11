from django.urls import path
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Manufacturer

class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = 'manufacturer_list.html'  # Change this to your desired template
    context_object_name = 'manufacturers'

class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = 'manufacturer_detail.html'  # Change this to your desired template
    context_object_name = 'manufacturer'

class ManufacturerCreateView(CreateView):
    model = Manufacturer
    template_name = 'manufacturer_form.html'  # Change this to your desired template
    fields = ['name', 'contact_person', 'email', 'phone']

class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    template_name = 'manufacturer_form.html'  # Change this to your desired template
    fields = ['name', 'contact_person', 'email', 'phone']

class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    template_name = 'manufacturer_confirm_delete.html'  # Change this to your desired template
    success_url = '/manufacturers/'  # Change this to the URL you want to redirect after deletion


