from django.urls import path
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'  # Change this to your desired template
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'  # Change this to your desired template
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'  # Change this to your desired template
    fields = ['name', 'description', 'unit_price', 'supplier', 'manufacturer']

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'  # Change this to your desired template
    fields = ['name', 'description', 'unit_price', 'supplier', 'manufacturer']

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'  # Change this to your desired template
    success_url = '/products/'  # Change this to the URL you want to redirect after deletion




