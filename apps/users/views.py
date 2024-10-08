from datetime import datetime
from django.contrib.auth import authenticate
from django.contrib.sessions.models import Session
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, Response as OpenApiResponse, TYPE_OBJECT, TYPE_STRING
from apps.users.api.serializers.token_obtain import CustomTokenObtainPairSerializer
from apps.users.api.serializers.user_serializers import UserReadOnlySerializer, UserSerializer, UserSwaggerResponseSerializer
from apps.users.models import User
# Create your views here.



class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    
    @swagger_auto_schema(
        operation_description="Login",
        request_body=CustomTokenObtainPairSerializer,
        responses={
            200: UserSwaggerResponseSerializer
        }
    )
    def post(self, request: Request, *args, **kwargs) -> Response:
        """autenticación de usuarios y generación de tokens.
        Si el usuario está correctamente autenticado, se serializará la info del usuario
        se activará la sesión de usuario y se responderá con tokens de autenticación JWT y de refresh

        Args:
            request (Request): Request POST con username y password

        Returns:
            Response
        """
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        user: User = authenticate(
            username=username,
            password=password,
        )
        if user is not None:
            login_serializer = self.get_serializer(data=request.data)
            if login_serializer.is_valid():
                if not user.is_active:
                    return Response(
                        {"message": "Este usuario no puede iniciar sesión"},
                        status=status.HTTP_401_UNAUTHORIZED)
                user_serializer = UserReadOnlySerializer(instance=user)
                return Response({
                    "token": login_serializer.validated_data.get("access"),
                    "refresh_token": login_serializer.validated_data.get("refresh"),
                    "user": user_serializer.data,
                })
        return Response(
            {"message": "Usuario o contraseña incorrectos"},
            status=status.HTTP_400_BAD_REQUEST)

class Logout(generics.GenericAPIView):
    permission_classes = [IsAuthenticated,]
    
    
    def delete_all_sessions(self, user:User) -> None:
        """Elimina todas las sesiones del usuario suministrado

        Args:
            user (User): Usuario al que se le eliminarán las sesiones.
        """
        all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
        if all_sessions.exists():
            for session in all_sessions:
                session_data = session.get_decoded()
                if user.id == int(session_data.get("_auth_user_id")):
                    session.delete()
        
    
    def post(self, request:Request, *args, **kwargs):
        
        user: User = request.user
        if user is not None:
            RefreshToken.for_user(user=user)
            
            # Si deseo cerrar el resto de sesiones, descomenta la sig linea
            self.delete_all_sessions(user)
            
            return Response({
                "message": "Se ha cerrado la sesión"
            }, status.HTTP_200_OK)
        
        return Response({"message": "El usuario no existe"}, status.HTTP_400_BAD_REQUEST)