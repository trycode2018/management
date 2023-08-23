from rest_framework import viewsets,mixins
from inventory_management.models.suppliers import Supplier
from inventory_management.serializers.supplier_serializer import SupplierSerializer

class SupplierView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
    
