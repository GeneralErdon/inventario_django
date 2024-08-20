from decimal import Decimal
from apps.base.tests import BaseFactory
from apps.productos.models import Product
from tests.factories.productos.category_factory import CategoryFactory
from tests.factories.productos.supplier_factory import SupplierFactory

class ProductFactory(BaseFactory):
    model = Product
    
    def get_json(self, instances=False) -> dict[str, str]:
        f_name = self.faker.first_name().lower()
        l_name = self.faker.last_name().lower()
        measurement_choices = [
            Product.MEASUREMENT_GRAMOS,
            Product.MEASUREMENT_PAQUETE,
            Product.MEASUREMENT_MILILITROS,
            Product.MEASUREMENT_LITROS,
            Product.MEASUREMENT_LIBRAS,
            Product.MEASUREMENT_KILOS,
            Product.MEASUREMENT_UNIDAD
        ]
        
        supplier = SupplierFactory().create()
        
        return {
            "code": f_name[:3] + l_name[:3] + f"-{self.faker.random.randint(0, 20)}",
            "name": self.faker.paragraph(nb_sentences=1)[:20],
            "description": self.faker.paragraph(nb_sentences=5)[:100],
            "cost": self.faker.random.randint(50, 100),
            "price": self.faker.random.randint(100, 500),
            "measurement": self.faker.random.choice(measurement_choices),
            "quantity": self.faker.random.randint(0, 100),
            "supplier": supplier if instances else supplier.pk,
            "changed_by": 1,
        }
    
    def create_bulk(self, count:int) -> list[Product]:
        """Método para la creación masiva de items en una sola consulta

        Args:
            count (int): Cantidad de items a crear

        Returns:
            list[Model]: Modelos creados
        """
        model_class = self.get_model()
        items = [ model_class(**self.get_json(instances=True)) for _ in range(count) ]
        return model_class.objects.bulk_create(items)
    
    