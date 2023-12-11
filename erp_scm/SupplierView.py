from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Supplier

class SupplierListView(ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'

class SupplierDetailView(DetailView):
    model = Supplier 
    template_name = 'supplier_detail.html'
    context_object_name = 'supplier'

class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'supplier_form.html'
    field = '__all__'
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
    model = Supplier 
    template_name = 'supplier_form_update.html'
    field = '__all__'
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(DeleteView):
    model = Supplier 
    template_name = 'supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier_list')