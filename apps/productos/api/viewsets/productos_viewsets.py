

from apps.base.viewsets.viewsets_generics import GenericModelViewset
from apps.productos.api.serializers.productos_serializers import ProductModelSerializer, ProductReadOnlySerializer


class ProductViewSet(GenericModelViewset):
    serializer_class = ProductModelSerializer
    read_only_serializer = ProductReadOnlySerializer
    
    prefetch_related_qs = [
        "categories"
    ]
    select_related_qs = [
        "supplier"
    ]
    
    search_fields = [
        "name",
        "supplier__identification",
    ]