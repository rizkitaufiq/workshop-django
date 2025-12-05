from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from products.forms.product_form import ProductForm
from products.services.product_service import update_product

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            update_product(form)
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/update.html', {'form': form})