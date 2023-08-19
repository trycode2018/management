from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    