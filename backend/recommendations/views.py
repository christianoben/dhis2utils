from django.db import models
from rest_framework import viewsets, permissions
from .models import RecommendedMatch
from .serializers import RecommendedMatchSerializer


class RecommendedMatchViewSet(viewsets.ModelViewSet):
    queryset = RecommendedMatch.objects.select_related('pool', 'player1', 'player2')
    serializer_class = RecommendedMatchSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        pool_id = self.request.query_params.get('pool_id')
        player_id = self.request.query_params.get('player_id')
        if pool_id:
            queryset = queryset.filter(pool_id=pool_id)
        if player_id:
            queryset = queryset.filter(models.Q(player1_id=player_id) | models.Q(player2_id=player_id))
        return queryset
