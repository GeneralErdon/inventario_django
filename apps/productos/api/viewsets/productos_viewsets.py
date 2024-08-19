

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
    
    # Se puede filtrar mediante el Query Param de ?search=
    # Los campos de Name, por identificación del proveedor, codigo de producto
    # nombre de las categorías también.
    # Ejemplo: localhost:8000/productos/producto/?search=carne
    search_fields = [
        "name",
        "code",
        "supplier__identification",
        "categories__name",
    ]