from rest_framework import serializers
from .models import User, Player, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'full_name', 'phone_number', 'email', 'is_active', 'roles']
        read_only_fields = ['is_active']

    def get_roles(self, obj):
        return [user_role.role.name for user_role in obj.user_roles.select_related('role')]


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'display_name', 'phone_number', 'preferred_pool', 'photo_url', 'user', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
