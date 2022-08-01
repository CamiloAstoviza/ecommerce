from django.contrib import admin
from .models import Product

@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display = ['Refresco','Description','CONT']