from pyexpat import model
from django.db import models


class Product(models.Model):
    
        Refresco = models.CharField(max_length=40)
        Description = models.CharField(max_length=200,blank=True,null=True)
        CONT = models.FloatField()
        

