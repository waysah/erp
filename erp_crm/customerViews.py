from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Customer
from django.urls import reverse_lazy

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['name', 'email', 'phone']
    success_url = reverse_lazy('customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['name', 'email', 'phone']
    success_url = reverse_lazy('customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')
