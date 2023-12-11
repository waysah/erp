from django.http import HttpResponse
from django.urls import path 
from . import views 
from . SupplierView import SupplierCreateView, SupplierDeleteView
from . SupplierView import SupplierDetailView, SupplierListView
from . SupplierView import SupplierUpdateView

urlpatterns = [
    path('', views.erp_scm, name="erp_scm"),

    # Urls for suppliers
    path('supplier/', SupplierListView.as_view(), name='services'),
    path('supplier/new/', SupplierCreateView.as_view(), name='supplier_create'),
    path('supplier/<int:pk>/edit/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),


]