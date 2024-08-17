from rest_framework import serializers

from apps.users.models import User
from apps.users.typing import _TUserValidatedData

class UserReadOnlySerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        for field in fields:
            fields[field].read_only = True
        return fields
    class Meta:
        model = User
        exclude = ("password",)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("last_login",)
    
    def validate_groups(self, groups:list[str]):
        if not self.instance: # if Patch
            return None
        
        return groups
    def validate_user_permissions(self, perms:list[str]):
        if not self.instance:
            return None
        
        return perms
    
    def set_user_password(self, user:User, password:str):
        user.set_password(password)
        user.save()
        return user
    
    
    def create(self, validated_data:_TUserValidatedData) -> User:
        
        groups = validated_data.pop("groups", []) or []
        user_permissions = validated_data.pop("user_permissions", []) or []
        
        user_created = User(**validated_data)
        user_created = self.set_user_password(user_created, validated_data["password"])
        
        user_created.groups.set(groups)
        user_created.user_permissions.set(user_permissions)
        
        return user_created
    
    def update(self, instance, validated_data:_TUserValidatedData) -> User:
        user_updated:User = super().update(instance, validated_data)
        if "password" in validated_data:
            user_updated = self.set_user_password(user_updated, validated_data["password"])
        return user_updated

