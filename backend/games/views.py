from rest_framework import viewsets, permissions
from .models import Game
from .serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.select_related(
        'pool', 'player1', 'player2', 'initiated_by', 'accepted_by', 'winner'
    )
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]
