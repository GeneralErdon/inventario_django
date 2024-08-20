from apps.base.tests import BaseFactory
from apps.productos.models import Supplier

class SupplierFactory(BaseFactory):
    model = Supplier
    
    def get_json(self) -> dict[str, str]:
        return {
            "name": f"{self.faker.first_name()} {self.faker.last_name()}",
            "nature": self.faker.random.choice(
                [Supplier.NATURE_EXTRANJERO, Supplier.NATURE_JURIDICO, Supplier.NATURE_VENEZOLANO]
                ),
            "identification": self.faker.random.randint(1_000_000, 99_999_999),
            "email": self.faker.email(),
            "changed_by": 1,
        }
    
    