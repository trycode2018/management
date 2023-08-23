from rest_framework import serializers
from inventory_management.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"