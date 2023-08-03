from django.shortcuts import render

from .models import Product

# Create your views here.
def index(request):
    
    return render(request, 'base.html')


def products(request):
    products_list = Product.objects.all()
    return render(request, 'store/products_list.html', {'products_list':products_list})
