from rest_framework import viewsets,mixins
from .models import Supplier
from .serializers import SupplierSerializer

# Create your views here.

class SupplierView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer