from rest_framework import serializers

from apps.base.serializers import BaseModelSerializer, BaseReadOnlySerializer
from apps.productos.models import Product

class ProductModelSerializer(BaseModelSerializer):
    class Meta:
        model = Product
        exclude = ("created_date", "modified_date", "deleted_date", "status", "changed_by")
    
    def validate_quantity(self, value:int) -> int:
        if value < 0:
            raise serializers.ValidationError("No puedes tener valores negativos en almacén")
        return value

class ProductReadOnlySerializer(BaseReadOnlySerializer):
    class Meta:
        model = Product
        fields = "__all__"