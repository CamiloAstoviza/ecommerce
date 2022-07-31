from multiprocessing import context
from django.shortcuts import render
from products.models import Product
from django.http import request
def Create_product(request):
    new_product = Product.objects.create(Refresco = 'Sprite',Description = 'te hace eruptar',CONT= 2.0)
    context = {
        'new_product':new_product
    }
    return render(request,'product/new_product.html',context=context)


def allproducts(request):
    Allproducts = Product.objects.all()
    context = {
        'allproducts': Allproducts
    }
    return render(request,'product/all_products.html',context=context)
