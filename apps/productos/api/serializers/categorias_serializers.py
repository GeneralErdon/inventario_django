from rest_framework import serializers

from apps.base.serializers import BaseModelSerializer, BaseReadOnlySerializer
from apps.productos.models import Category

class CategoryModelSerializer(BaseModelSerializer):
    class Meta:
        model = Category
        exclude = ("created_date", "modified_date", "deleted_date", "status",)
    
    def validate_name(self, name:str) -> str:
        # Convierte esta propiedad a mayúscula para siempre consistencia de datos
        return name.upper()

class CategoryReadOnlySerializer(BaseReadOnlySerializer):
    class Meta:
        model = Category
        fields = "__all__"