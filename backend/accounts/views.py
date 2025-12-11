from rest_framework import viewsets, permissions
from .models import User, Player
from .serializers import UserSerializer, PlayerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.select_related('preferred_pool', 'user')
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]
