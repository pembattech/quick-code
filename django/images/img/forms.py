from django import forms
from .models import Product, ProductGallery

class ProductGalleryForm(forms.ModelForm):
    class Meta:
        model = ProductGallery
        fields = ['product', 'image']

ProductGalleryFormSet = forms.inlineformset_factory(Product, ProductGallery, form=ProductGalleryForm, extra=1, can_delete=True)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'slug', 'description', 'price', 'stock', 'is_available']

