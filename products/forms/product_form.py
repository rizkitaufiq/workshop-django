from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama produk...'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Harga produk'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Deskripsi produk'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Nama produk wajib diisi.")
        if len(name) < 3:
            raise forms.ValidationError("Nama produk harus lebih dari 3 karakter.")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise forms.ValidationError("Harga wajib diisi.")
        if price <= 0:
            raise forms.ValidationError("Harga harus lebih dari 0.")
        return price

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description) < 10:
            raise forms.ValidationError("Deskripsi harus minimal 10 karakter.")
        return description