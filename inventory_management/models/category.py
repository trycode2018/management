from django.db import models
from .models import Base


class Category(Base):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
   