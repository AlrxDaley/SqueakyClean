from django.shortcuts import render, get_object_or_404
from products.models import Product
from .models import Special

# Create your views here.

def index(request):
    
    specials = Special.objects.first()
    product1 = get_object_or_404(Product, pk=specials.special_id_1)
    product2 = get_object_or_404(Product, pk=specials.special_id_2)
    product3 = get_object_or_404(Product, pk=specials.special_id_3)

    context = {
        'product1': product1,
        'product2': product2,
        'product3': product3
    }
    return render(request, 'store/index.html', context)

def about(request):
    context = {}
    return render(request, 'store/about.html', context)

def shop(request):
    context = {}
    return render (request, 'store/shop.html', context)

def shopSingle(request):
    context = {}
    return render (request, 'store/shopSingle.html', context)

def contact(request):
    context = {}
    return render (request, 'store/contact.html', context)
