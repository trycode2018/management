from rest_framework import serializers
from inventory_management.models.products import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"