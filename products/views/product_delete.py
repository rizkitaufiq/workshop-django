from django.shortcuts import redirect, get_object_or_404
from products.models import Product
from products.services.product_service import delete_product

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    delete_product(product)
    return redirect('product_list')