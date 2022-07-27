from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from numpy import product
from prometheus_client import CONTENT_TYPE_LATEST
from products.models import Product

def Create_product(request):
    new_product = Product.objects.create(Refresco = 'Coca cola',Description = 'La de siempre al mejor precio',CONT= 2.0)
    context = {
        'new_product':new_product
    }
    return render(request,'new_product.html',context=context)