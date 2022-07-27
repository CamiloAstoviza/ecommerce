from django.urls import URLPattern, path
from products.views import Create_product
urlpatterns = [
    path('new-product/',Create_product,name='create_product')
]