from apps.productos.models import Supplier
from tests.factories.productos.supplier_factory import SupplierFactory
from tests.test_setup import TestSetup
from rest_framework import status
from rest_framework.response import Response
import json

class SuppliersTestCase(TestSetup):
    ENDPOINT = "/productos/supplier/"
    model = Supplier
    
    def test_list_suppliers(self):
        SupplierFactory().create_bulk(200)
        
        response = self.client.get(
            path=self.ENDPOINT 
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 200)
        
        self.Messages.ok("TEST LIST SUPPLIERS 1 OK")
    
    def test_retrieve_supplier(self):
        
        supplier: Supplier = SupplierFactory().create()
        
        response: Response = self.client.get(
            self.ENDPOINT + f"{supplier.id}/"
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(supplier.id, response.data["id"])
        
        self.Messages.ok("TEST RETRIEVE SUPPLIER 1 OK")
    
    def test_create_supplier(self):
        
        supplier_json: dict = SupplierFactory().get_json()
        
        response: Response = self.client.post(
            self.ENDPOINT,
            data=json.dumps(supplier_json),
            content_type="application/json",
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        exists = Supplier.objects.filter(name__icontains=supplier_json["name"]).exists()
        
        self.assertTrue(exists, "No existe el item")
        
        self.Messages.ok("TEST CREATE SUPPLIER 1 OK")
    
    def test_update_supplier(self):
        
        supplier: Supplier = SupplierFactory().create()
        new_name = "NewSupplierName"
        
        
        self.assertNotEqual(supplier.name, new_name)
        
        response: Response = self.client.patch(
            self.ENDPOINT + f"{supplier.id}/",
            data=json.dumps({
                "name": new_name
            }),
            content_type="application/json"
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], new_name.upper())
        
        self.Messages.ok("TEST UPDATE SUPPLIER 1 OK")
