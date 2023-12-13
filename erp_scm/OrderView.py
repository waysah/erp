from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView
from django.urls import reverse_lazy
from . models import Order

class OrderListView(ListView):
    model  = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_form.html'
    fields = '__all__'

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_form_update.html'
    fields = '__all__'

class OrderDeleteView(DeleteView):
    model = Order 
    template_name = 'order_confirm_delete.html'
    success_url  = '/orders/'