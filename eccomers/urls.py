
from django.contrib import admin
from django.urls import path,include
from numpy import product
from .views import index


urlpatterns = [
    path('',index,name='inicio'),
    path('admin/', admin.site.urls),
    path('product/',include('products.urls')),
    path('all_products/',include('products.urls')),
    path('formulario/',include('products.urls')),
    path('search/',include('products.urls')),
    path('delete/',include('products.urls')),
    path('update/',include('products.urls')),
    path('users/',include('users.urls')),
]
