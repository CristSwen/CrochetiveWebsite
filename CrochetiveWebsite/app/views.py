"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import ApparelProduct, ToysProduct, PetsProduct
from .forms import ApparelForm, ToysForm, PetsForm
import requests
from django.contrib import admin


def home(request):
    return render(request, 'app/index.html')

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def shop(request):
    """Renders the Shop page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/shop.html',
        {
            'title':'Shop',
            'message':'The Shop',
            'year':datetime.now().year,
            }
        )

def shop_apparel(request):
    """Renders the Shop page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/apparel_shop.html',
        {
            'title':'Shop',
            'message':'The Shop',
            'year':datetime.now().year,
            }
        )


"""View CREATE functions """

def create_product_apparel(request):
    form = ApparelForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('shop_apparel')
    content = {'form': form}
    return render(request, 'app/create_apparel.html', content)

def create_product_toys(request):
    form = ToysForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('shop_apparel')
    content = {'form': form}
    return render(request, 'app/create_toys.html', content)

def create_product_pets(request):
    form = PetsForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('shop_apparel')
    content = {'form': form}
    return render(request, 'app/create_pets.html', content)


""" Views for the STORED products and will allow the products to show on the webpage."""

def stored_apparels(request):
    entry = ApparelProduct.objects.all()
    content = {'entry': entry}
    return render(request, 'app/apparel_shop.html', content)

def stored_pets(request):
    entry2 = PetsProduct.objects.all()
    content = {'entry2': entry2}
    return render(request, 'app/index.html', content)

def stored_toys(request):
    entry3 = ToysProduct.objects.all()
    content = {'entry3': entry3}
    return render(request, 'app/index.html', content)





def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('app/index.html')
    else:
        form = ProductForm(instance=product)
    return redner(request, "app/edit_product.html", {'form': form, 'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('app/index.html')
    return render(request, 'app/delete_product.html', {'product': product})

admin.site.register(ApparelProduct)
admin.site.register(ToysProduct)
admin.site.register(PetsProduct)