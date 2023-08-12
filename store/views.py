from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView


from .models import Product, Brand, SubCategory, Category
from .forms import ProductForm

# Create your views here.
# def index(request):
    
#     return render(request, 'base.html')


def products(request):
    products_list = Product.objects.all()
    return render(request, 'store/products_list.html', {'products_list':products_list})


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_details.html', {'product':product})




def add_product(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('login')

        else:
            form = ProductForm()

        return render(request, 'store/product_add.html',{'form':form})
    else: 
        return redirect('products')




def edit_product(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('products')

        else:
            form = ProductForm(instance=product)

        return render(request, 'store/product_add.html',{'form':form})
    else : 
        return redirect('products')


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products')


class CreateCategory(CreateView):
    
    model = Category
    fields = ['image', 'name']
    success_url = '/products'

class CreateSubCategory(CreateView):
    model = SubCategory
    fields = ['category', 'name']
    success_url = '/products'



class CreateBrand(CreateView):
    model = Brand
    fields = ['name']
    success_url = '/products'



