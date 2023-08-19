from django.db import models

# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True    


class Category(Base):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
