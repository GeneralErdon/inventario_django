

from apps.productos.models import Category
from tests.factories.productos.category_factory import CategoryFactory
from tests.test_setup import TestSetup
from rest_framework import status
from rest_framework.response import Response
import json

class CategoriesTestCase(TestSetup):
    ENDPOINT = "/productos/category/"
    model = Category
    
    def test_list_categories(self):
        CategoryFactory().create_bulk(200)
        
        response = self.client.get(
            path=self.ENDPOINT 
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 200)
        
        self.Messages.ok("TEST LIST CATEGORIES 1 OK")
    
    def test_retrieve_category(self):
        
        category: Category = CategoryFactory().create()
        
        response: Response = self.client.get(
            self.ENDPOINT + f"{category.id}/"
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(category.id, response.data["id"])
        
        self.Messages.ok("TEST RETRIEVE CATEGORY 1 OK")
    
    def test_create_category(self):
        
        category_json: dict = CategoryFactory().get_json()
        
        response: Response = self.client.post(
            self.ENDPOINT,
            data=json.dumps(category_json),
            content_type="application/json",
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        
        exists = Category.objects.filter(name__icontains=category_json["name"]).exists()
        self.assertTrue(exists, "No existe el item")
        
        self.Messages.ok("TEST CREATE CATEGORY 1 OK")
    
    def test_update_category(self):
        
        category: Category = CategoryFactory().create()
        new_name = "NewCategoryName"
        
        self.assertNotEqual(category.name, new_name)
        
        response: Response = self.client.patch(
            self.ENDPOINT + f"{category.id}/",
            data=json.dumps({
                "name": new_name
            }),
            content_type="application/json"
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], new_name.upper())
        
        self.Messages.ok("TEST UPDATE CATEGORY 1 OK")


