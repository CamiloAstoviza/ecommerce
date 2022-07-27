from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from numpy import product
from prometheus_client import CONTENT_TYPE_LATEST
from products.models import Product

def Create_product(request):
    new_person = Product.objets.create(Refresco = '',Description = '',CONT= 1)
    context = {
        'new_person':new_person
    }
    return render(request,'new_product.html',context=context)