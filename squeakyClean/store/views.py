from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'store/index.html', context)

def about(request):
    context = {}
    return render(request, 'store/about.html', context)