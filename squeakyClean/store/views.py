from django.shortcuts import render, get_object_or_404
from django.urls import path
import os
from django.conf import settings
from django.conf.urls.static import static
from products.models import Product, Category
from .models import Special

# Create your views here.

def index(request):
    
    specials = Special.objects.first()
    product1 = get_object_or_404(Product, pk=specials.special_id_1)
    product2 = get_object_or_404(Product, pk=specials.special_id_2)
    product3 = get_object_or_404(Product, pk=specials.special_id_3)
    
    categories = Category.objects.all
    
    context = {
        'product1': product1,
        'product2': product2,
        'product3': product3,
        'categories':categories,
    }
    return render(request, 'store/index.html', context)

def about(request):
    categories = Category.objects.all
    
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path)

    
    context = {
        'categories':categories,
        'images' : img_list
    }

    return render(request, 'store/about.html', context)

def shop(request):
    context = {}
    return render (request, 'store/shop.html', context)

def contact(request):
    categories = Category.objects.all
    
    context = {
        'categories':categories
    }

    return render (request, 'store/contact.html', context)
