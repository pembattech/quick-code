from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductGallery
from .forms import ProductForm, ProductGalleryFormSet

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    gallery = ProductGallery.objects.filter(product=product)
    return render(request, 'product_detail.html', {'product': product, 'gallery': gallery})

def edit_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        formset = ProductGalleryFormSet(request.POST, request.FILES, instance=product)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('product_detail', slug=product.slug)
    else:
        form = ProductForm(instance=product)
        formset = ProductGalleryFormSet(instance=product)

    return render(request, 'edit_product.html', {'form': form, 'formset': formset, 'product': product})


# views.py
# views.py

from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm, ProductGalleryFormSet

from django.shortcuts import render, redirect
from .forms import ProductForm, ProductGalleryFormSet

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        formset = ProductGalleryFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            product = form.save()
            formset.instance = product
            formset.save()

            return redirect('product_detail', slug=product.slug)
    else:
        form = ProductForm()
        formset = ProductGalleryFormSet()

    return render(request, 'add_product.html', {'form': form, 'formset': formset})
