from unicodedata import name
from django.urls import URLPattern, path
from products.views import Create_product, Formulario, allproducts
urlpatterns = [
    path('newproduct/',Create_product,name='newproduct'),
    path('all_products/',allproducts,name='all_products'),
    path('formulario/',Formulario,name='formulario')
]