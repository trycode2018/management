from rest_framework import viewsets,mixins
from inventory_management.models.products import Product
from inventory_management.serializers.product_serializer import ProductSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
