from django.db import models

from apps.base.models import BaseModel

# Create your models here.
class Category(BaseModel):
    """
    Modelo para registrar las categorias de los productos
    """
    name = models.CharField(
        verbose_name="Nombre",
        help_text="Nombre de la categoría",
        max_length=50,
        unique=True,
        db_index=True,
    )
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Supplier(BaseModel):
    """Modelo del Proveedor del producto
    """
    NATURE_JURIDICO = "J"
    NATURE_VENEZOLANO = "V"
    NATURE_EXTRANJERO = "E"
    
    name = models.CharField(
        verbose_name="Nombre",
        help_text="Nombre del proveedor",
        max_length=150,
    )
    nature = models.CharField(
        verbose_name="Naturaleza",
        help_text="Naturaleza del proveedor, ya sea Juridico, Natural, Extranjero.",
        choices=(
            (NATURE_VENEZOLANO, "VENEZOLANO"),
            (NATURE_EXTRANJERO, "EXTRANJETO"),
            (NATURE_JURIDICO, "JURIDICO"),
        ),
        max_length=1,
        db_index=True,
    )
    
    identification = models.CharField(
        verbose_name="Identificación",
        help_text="RIF / Cedula de identidad",
        max_length=15,
        unique=True,
        db_index=True,
    )
    
    email = models.EmailField(
        verbose_name="Email",
        help_text="Email de contacto",
        null=True,
        blank=True,
    )
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

class Product(BaseModel):
    
    
    MEASUREMENT_LIBRAS = "LB"
    MEASUREMENT_GRAMOS = "GR"
    MEASUREMENT_KILOS = "KG"
    MEASUREMENT_LITROS = "LT"
    MEASUREMENT_MILILITROS = "ML"
    MEASUREMENT_UNIDAD = "UD"
    MEASUREMENT_PAQUETE = "PQ"
    
    
    code = models.CharField(
        verbose_name="Código",
        help_text="Código del producto.",
        max_length=50,
        unique=True,
        db_index=True,
    )
    
    name = models.CharField(
        verbose_name="Nombre",
        help_text="Nombre del producto",
        max_length=120,
        db_index=True
    )
    
    description = models.TextField(
        verbose_name="Descripción",
        help_text="Descripción del producto",
    )
    
    price = models.DecimalField(
        verbose_name="Precio (USD)",
        help_text="Precio de venta del producto en USD",
        decimal_places=2,
        max_digits=20,
    )
    
    cost = models.DecimalField(
        verbose_name="Costo (USD)",
        help_text="Costo de adquisición del producto en USD",
        decimal_places=2,
        max_digits=20,
    )
    
    quantity = models.DecimalField(
        verbose_name="Cantidad",
        help_text="Cantidad disponible o almacenada del producto en el inventario",
        max_digits=20,
        decimal_places=2,
        default=0
    )
    
    measurement = models.CharField(
        verbose_name="Unidad de medida",
        help_text="Unidad de medida para la cantidad. Ej. Gramos, Libras, Litros, Unidades, etc.",
        max_length=2,
        choices=(
            (MEASUREMENT_LIBRAS, "LIBRAS"),
            (MEASUREMENT_GRAMOS, "GRAMOS"),
            (MEASUREMENT_KILOS, "KILOGRAMOS"),
            (MEASUREMENT_LITROS, "LITROS"),
            (MEASUREMENT_MILILITROS, "MILILITROS"),
            (MEASUREMENT_UNIDAD, "UNIDAD"),
            (MEASUREMENT_PAQUETE, "PAQUETE"),
        ),
    )
    
    # Relaciones
    supplier = models.ForeignKey(
        to=Supplier, on_delete=models.RESTRICT
    ) 
    
    # un producto podría entrar en varias categorías, y una categoría podría estar presente en varios productos
    categories = models.ManyToManyField(to=Category)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'