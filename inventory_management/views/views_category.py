from rest_framework import viewsets,mixins
from inventory_management.models.category import Category
from inventory_management.serializers.category_serializer import CategorySerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer