from django.db import models
from .models import Base
from .category import Category
from .suppliers import Supplier

class Product(Base):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    barcode = models.CharField(max_length=25)
    category = models.ForeignKey(Category,related_name='products_categories',on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier,related_name='suppliers_products',on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
