from apps.base.tests import BaseFactory
from apps.productos.models import Product
from tests.factories.productos.category_factory import CategoryFactory
from tests.factories.productos.supplier_factory import SupplierFactory

class ProductFactory(BaseFactory):
    model = Product
    
    def get_json(self, w_instances=False) -> dict[str, str]:
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
        
        
        return {
            "code": f_name[:3] + l_name[:3] + f"-{self.faker.random.randint(0, 20)}",
            "name": self.faker.paragraph(nb_sentences=1),
            "description": self.faker.paragraph(nb_sentences=5),
            "cost": self.faker.random.random() * 10,
            "price": self.faker.random.random() * 20,
            "measurement": self.faker.random.choice(measurement_choices),
            "quantity": self.faker.random.randint(0, 100),
            
            "changed_by": 1,
        }
    
    