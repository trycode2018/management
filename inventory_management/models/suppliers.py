from django.db import models
from .models import Base


class Supplier(Base):
    providers_name = models.CharField(max_length=100)
    contact_information =models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'supplier'
        verbose_name_plural = 'suppliers'
