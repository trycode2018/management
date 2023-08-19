from django.db import models

# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True    
 

class Supplier(Base):
    providers_name = models.CharField(max_length=100)
    contact_information =models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'supplier'
        verbose_name_plural = 'suppliers'