from pyexpat import model
from tabnanny import verbose
from django.db import models


class Product(models.Model):
    
        Refresco = models.CharField(max_length=40,unique=True)
        Description = models.CharField(max_length=200,blank=True,null=True)
        CONT = models.FloatField()
        def __str__(self):
                return self.Refresco
        class Meta:
                verbose_name = 'Product'
                verbose_name_plural = 'Products'
