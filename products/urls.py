from django.urls import URLPattern, path
from products.views import Create_product
urlpatterns = [
    path('new_product/',Create_product,name='create_product')
]