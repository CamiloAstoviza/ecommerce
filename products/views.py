from multiprocessing import context
from django.shortcuts import render
from numpy import product
from products.models import Product
from django.http import request
from products.forms import Formulario
def Create_product(request):
    new_product = Product.objects.create (Refresco = 'Sprite',Description = 'te hace eruptar',CONT= 2.0)
    context = {
        'new_product':new_product
    }
    return render(request,'product/new_product.html',context=context)


def allproducts(request):
    Allproducts = Product.objects.all()
    context = {
        'Allproducts': Allproducts
    }
    return render(request,'product/all_products.html',context=context)

def formulario(request):

    if request.method == 'POST':
        miformulario = Formulario(request.POST)
        
        print(miformulario)



        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            nombre = Product(Refresco=informacion['refresco'],CONT=informacion['cont'])
            nombre.save()
            return render(request,'product/all_products.html')
    else:
        miformulario=Formulario()
    return render(request,'formulario/formulario.html',{"miformulario":miformulario})