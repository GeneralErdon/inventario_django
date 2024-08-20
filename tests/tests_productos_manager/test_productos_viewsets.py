from apps.productos.models import Product
from tests.factories.productos.category_factory import CategoryFactory
from tests.factories.productos.product_factory import ProductFactory
from tests.factories.productos.supplier_factory import SupplierFactory
from tests.test_setup import TestSetup
from rest_framework import status
from rest_framework.response import Response
import json

class ProductsTestCase(TestSetup):
    ENDPOINT = "/productos/product/"
    model = Product
    
    def test_list_products(self):
        ProductFactory().create_bulk(200)
        
        response = self.client.get(
            path=self.ENDPOINT 
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 200)
        
        self.Messages.ok("TEST LIST PRODUCTS 1 OK")
    
    def test_retrieve_product(self):
        
        product: Product = ProductFactory().create()
        
        response: Response = self.client.get(
            self.ENDPOINT + f"{product.id}/"
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(product.id, response.data["id"])
        
        self.Messages.ok("TEST RETRIEVE PRODUCT 1 OK")
    
    def test_create_product(self):
        
        product_json: dict = ProductFactory().get_json()
        
        
        
        response: Response = self.client.post(
            self.ENDPOINT,
            data=json.dumps(product_json),
            content_type="application/json",
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        
        exists = Product.objects.filter(name__icontains=product_json["name"]).exists()
        
        self.assertTrue(exists, "No existe el item")
        
        self.Messages.ok("TEST CREATE PRODUCT 1 OK")
    
    def test_update_product(self):
        
        product: Product = ProductFactory().create()
        new_name = "NewProductName"
        
        
        self.assertNotEqual(product.name, new_name)
        
        response: Response = self.client.patch(
            self.ENDPOINT + f"{product.id}/",
            data=json.dumps({
                "name": new_name,
            }),
            content_type="application/json"
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], new_name.upper())
        
        self.Messages.ok("TEST UPDATE PRODUCT 1 OK")
