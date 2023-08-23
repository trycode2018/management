from rest_framework import serializers
from inventory_management.models.suppliers import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
        