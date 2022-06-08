from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
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

