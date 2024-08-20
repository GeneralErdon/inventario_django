from apps.base.tests import BaseFactory
from apps.productos.models import Category

class CategoryFactory(BaseFactory):
    model = Category
    
    def get_json(self) -> dict[str, str]:
        return {
            "name": self.faker.paragraph(nb_sentences=2)[:49], # Maximo de 50 caracteres
            "changed_by": 1,
        }
    
    