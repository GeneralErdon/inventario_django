
from apps.base.viewsets.viewsets_generics import GenericModelViewset
from apps.productos.api.serializers.proveedores_serializers import SupplierModelSerializer, SupplierReadOnlySerializer


class SupplierViewSet(GenericModelViewset):
    serializer_class = SupplierModelSerializer
    read_only_serializer = SupplierReadOnlySerializer
    
    
    search_fields = [
        "name",
        "identification",
        
    ]