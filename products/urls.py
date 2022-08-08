from re import U
from unicodedata import name
from django.urls import URLPattern, path
from products.views import Create_product, formulario, allproducts,search,delete_product,update
urlpatterns = [
    path('newproduct/',Create_product,name='newproduct'),
    path('all_products/',allproducts,name='all_products'),
    path('formulario/',formulario,name='formulario'),
    path('search/',search,name='search'),
    path('delete/<int:pk>',delete_product,name='delete'),
    path('update/<int:pk>',update,name='update')
]