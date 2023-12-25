from django.urls import path
from .views import product_detail, add_product, edit_product

urlpatterns = [
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<slug:slug>/', edit_product, name='edit_product'),
]
