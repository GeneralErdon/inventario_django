from apps.base.router import CustomRouter
from apps.productos.api.viewsets.categorias_viewsets import CategoryViewSet
from apps.productos.api.viewsets.productos_viewsets import ProductViewSet
from apps.productos.api.viewsets.proveedores_viewsets import SupplierViewSet

router = CustomRouter()
# añadir rutas
router.register(r'product', ProductViewSet, basename="product-viewset")
router.register(r'supplier', SupplierViewSet, basename="supplier-viewset")
router.register(r'category', CategoryViewSet, basename="category-viewset")

urlpatterns = router.urls