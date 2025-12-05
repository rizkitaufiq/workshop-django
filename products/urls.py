from django.urls import path
from products.views.product_list import product_list
from products.views.product_create import product_create
from products.views.product_update import product_update
from products.views.product_delete import product_delete

urlpatterns = [
    path('', product_list, name='product_list'),
    path('create/', product_create, name='product_create'),
    path('update/<int:pk>/', product_update, name='product_update'),
    path('delete/<int:pk>/', product_delete, name='product_delete'),
]