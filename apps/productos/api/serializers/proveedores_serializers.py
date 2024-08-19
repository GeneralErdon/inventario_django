from rest_framework import serializers

from apps.base.serializers import BaseModelSerializer, BaseReadOnlySerializer
from apps.productos.models import Supplier

class SupplierModelSerializer(BaseModelSerializer):
    class Meta:
        model = Supplier
        exclude = ("created_date", "modified_date", "deleted_date", "status", )
    
    def validate_name(self, name:str) -> str:
        # Convierte esta propiedad a mayúscula para siempre consistencia de datos
        return name.upper()

class SupplierReadOnlySerializer(BaseReadOnlySerializer):
    class Meta:
        model = Supplier
        fields = "__all__"