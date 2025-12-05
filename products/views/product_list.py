from django.shortcuts import render
from products.services.product_service import get_all_products

def product_list(request):
    products = get_all_products()
    return render(request, 'products/list.html', {'products': products})