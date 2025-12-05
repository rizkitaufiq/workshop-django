from products.models import Product

def get_all_products():
    return Product.objects.all().order_by('-created_at')

def get_product(pk):
    return Product.objects.get(pk=pk)

def create_product(form):
    return form.save()

def update_product(form):
    return form.save()

def delete_product(product):
    product.delete()