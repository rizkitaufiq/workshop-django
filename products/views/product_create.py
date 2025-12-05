from django.shortcuts import render, redirect
from products.forms.product_form import ProductForm
from products.services.product_service import create_product

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            create_product(form)
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/create.html', {'form': form})