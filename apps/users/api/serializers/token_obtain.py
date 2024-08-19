from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Clase para sobreescribir el serializador de Usuario
    especialmente diseñado para los tokens
    """
    
    pass

