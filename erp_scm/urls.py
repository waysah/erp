from django.http import HttpResponse
from django.urls import path 
from . import views 
from . SupplierView import SupplierCreateView, SupplierDeleteView
from . SupplierView import SupplierDetailView, SupplierListView
from . SupplierView import SupplierUpdateView
from . ManufacturerView import *
from . ProductView import *


urlpatterns = [
    path('', views.erp_scm, name="erp_scm"),

    # Urls for suppliers
    path('supplier/', SupplierListView.as_view(), name='services'),
    path('supplier/new/', SupplierCreateView.as_view(), name='supplier_create'),
    path('supplier/<int:pk>/edit/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),

    # Urls for Manufacturers
    path('manufacturers/', ManufacturerListView.as_view(), name='manufacturer_list'),
    path('manufacturer/<int:pk>/', ManufacturerDetailView.as_view(), name='manufacturer_detail'),
    path('manufacturer/create/', ManufacturerCreateView.as_view(), name='manufacturer_create'),
    path('manufacturer/<int:pk>/update/', ManufacturerUpdateView.as_view(), name='manufacturer_update'),
    path('manufacturer/<int:pk>/delete/', ManufacturerDeleteView.as_view(), name='manufacturer_delete'),

    # Urls for Products
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),



]