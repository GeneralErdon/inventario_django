from apps.users.models import User
from rest_framework import status
from rest_framework.response import Response
from tests.factories.users.user_factory import UsersFactory
from tests.test_setup import TestSetup
import json


class UsersTestCase(TestSetup):
    ENDPOINT = "/users/user/"
    model = User
    
    
    def test_list_users(self):
        UsersFactory().create_bulk(200)
        
        response = self.client.get(
            path=self.ENDPOINT 
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.Messages.ok("TEST LIST USERS 1 OK")
    
    def test_retrieve_users(self):
        
        user:User = UsersFactory().create()
        
        response: Response = self.client.get(
            self.ENDPOINT + f"{user.id}/"
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user.id, response.data["id"])
        
        self.Messages.ok("TEST RETRIEVE USERS 1 OK")
    
    def test_create_users(self):
        
        user_json:dict = UsersFactory().get_json()
        
        response: Response = self.client.post(
            self.ENDPOINT,
            data=json.dumps(user_json),
            content_type="application/json",
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        exists = User.objects.filter(username=user_json["username"]).exists()
        
        self.assertTrue(exists, "Not exists")
        
        self.Messages.ok("TEST CREATE USERS 1 OK")
    
    def test_update_users(self):
        
        user:User = UsersFactory().create()
        new_first_name = "LeandroFERMIN"
        
        self.assertNotEqual(user.first_name, new_first_name)
        
        response:Response = self.client.patch(
            self.ENDPOINT + f"{user.id}/",
            data=json.dumps({
                "first_name": new_first_name
            }),
            content_type="application/json"
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(response.data["first_name"], new_first_name)
        
        self.Messages.ok("TEST UPDATE USERS 1 OK")
    
    
    def test_delete_users(self):
        user = UsersFactory().create()
        
        response = self.client.delete(
            path=self.ENDPOINT + f"{user.pk}/",
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        user = User.objects.filter(is_active=False, pk=user.pk).first()
        self.assertNotEqual(user, None,)
        self.assertFalse(user.is_active)
        
        self.Messages.ok("TEST DELETE USERS 1 OK")