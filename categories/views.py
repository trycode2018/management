from rest_framework import viewsets, mixins
from .models import Category
from .serializers import CategorySerializer


# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer