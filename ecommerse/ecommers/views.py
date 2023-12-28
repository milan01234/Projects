
from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
# views.py


def product_spect(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    return render(request, 'product_spect.html', {'product': product})


# Create your views here.
