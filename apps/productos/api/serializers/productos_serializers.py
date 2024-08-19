from decimal import Decimal
from typing import Any
from rest_framework import serializers

from apps.base.serializers import BaseModelSerializer, BaseReadOnlySerializer
from apps.productos.api.serializers.categorias_serializers import CategoryReadOnlySerializer
from apps.productos.models import Product

class ProductModelSerializer(BaseModelSerializer):
    class Meta:
        model = Product
        exclude = ("created_date", "modified_date", "deleted_date", "status",)
    
    def validate_name(self, name:str) -> str: 
        # Convierte siempre la propiedad a mayúsculas para tener siempre la consistencia de datos igual
        return name.upper()
    
    def validate_quantity(self, qty:Decimal) -> Decimal:
        # Validando que no se tenga almacenados productos en negativo
        if qty < 0:
            raise serializers.ValidationError("No puedes tener valores negativos en almacén")
        
        return qty
    
    def validate(self, validated_data:dict[str,Any]):
        
        measurement:str = validated_data.get("measurement", None)
        qty:Decimal = validated_data.get("quantity", None)
        
        if self.instance: # En caso que sea un PATCH o PUT para actualizar
            measurement = self.instance.measurement if not measurement else measurement
            qty = self.instance.quantity if not qty else qty
        
        # Validando que si la unidad de medida es en unidades o paquetes, la cantidad del producto sea Entero
        if measurement in [Product.MEASUREMENT_UNIDAD, Product.MEASUREMENT_PAQUETE] and qty.to_integral_value() != qty:
            raise serializers.ValidationError("Un producto que se vende por unidades o paquetes no puede tener una cantidad en decimal")
        
        return validated_data

class ProductReadOnlySerializer(BaseReadOnlySerializer):
    categories = CategoryReadOnlySerializer(many=True)
    class Meta:
        model = Product
        fields = "__all__"