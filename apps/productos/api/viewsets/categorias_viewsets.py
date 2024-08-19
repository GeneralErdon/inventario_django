
from apps.base.viewsets.viewsets_generics import GenericModelViewset
from apps.productos.api.serializers.categorias_serializers import CategoryModelSerializer, CategoryReadOnlySerializer


class CategoryViewSet(GenericModelViewset):
    serializer_class = CategoryModelSerializer
    read_only_serializer = CategoryReadOnlySerializer
    
    
    search_fields = [
        "name",
    ]