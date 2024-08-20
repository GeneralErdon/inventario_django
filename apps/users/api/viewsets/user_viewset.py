from apps.base.viewsets.viewsets_generics import GenericModelViewset
from apps.users.api.serializers.user_serializers import UserReadOnlySerializer, UserSerializer

class UserModelViewset( GenericModelViewset):
    serializer_class = UserSerializer
    read_only_serializer = UserReadOnlySerializer
    search_fields = [
        "username",
        "first_name",
        "last_name",
    ]
    
    prefetch_related_qs = [
        "groups__content_type",
        "user_permissions__content_type",
        "logentry_set__content_type"
    ]
    
    def get_status_field(self) -> str: 
        # la propiedad del estado del usuario es is_active, define si está activo o inactivo
        return "is_active"