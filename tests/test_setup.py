from faker import Faker
from rest_framework.test import APITestCase
from rest_framework import status
from apps.base.utils import MessageManager as MM
from apps.users.models import User


class TestSetup(APITestCase):
    """TestSetup para realizar los test case como super usuario
    Para más información acerca de los test case visitar el siguiente video:
    https://www.youtube.com/watch?v=A4eQtTuhrpw
    """
    Messages = MM
    def setUp(self) -> None:
        
        self.LOGIN_ENDPOINT = "/login/"
        
        fake = Faker()
        
        self.super_user:User = User.objects.create_superuser(
            username="developer",
            password="developer",
            email=fake.email(),
        )
        
        
        self.super_token = self.getToken("developer")
        self.setToken(self.super_token)
        
        return super().setUp()
    
    def getToken(self, username: str, password:str = "developer") -> str:
        """Obtiene el token realizando una peticion interna a la vista de Login

        Args:
            username (str): Username al que se sacará el token
            password (str, optional): Contraseña. Defaults to "developer".

        Returns:
            str: Token de acceso
        """
        response = self.client.post(
            path=self.LOGIN_ENDPOINT,
            data={
                "username":username,
                "password": password,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Ese usuario no existe")
        return response.data["token"]
    
    def setToken(self, token:str):
        self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {token}")