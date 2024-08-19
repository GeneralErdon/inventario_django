from rest_framework import serializers

from apps.base.serializers import BaseModelSerializer, BaseReadOnlySerializer
from apps.productos.models import Supplier

class CategoryModelSerializer(BaseModelSerializer):
    class Meta:
        model = Supplier
        exclude = ("created_date", "modified_date", "deleted_date", "status", "changed_by")

class CategoryReadOnlySerializer(BaseReadOnlySerializer):
    class Meta:
        model = Supplier
        fields = "__all__"