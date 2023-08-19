from django.db import models
from categories.models import Category
from suppliers.models import Supplier

# Create your models here. 
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True    
           
class Product(Base):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    barcode = models.CharField(max_length=25)
    category = models.ForeignKey(Category,related_name='products_categories',on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier,related_name='suppliers_categories',on_delete=models.CASCADE)
    unitprice = models.DecimalField(max_digits=10,decimal_places=2)
    
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
