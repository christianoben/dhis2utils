from rest_framework import viewsets, permissions
from .models import LeaderboardEntry
from .serializers import LeaderboardEntrySerializer


class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.select_related('player')
    serializer_class = LeaderboardEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        scope_type = self.request.query_params.get('scope_type')
        period_type = self.request.query_params.get('period_type')
        if scope_type:
            queryset = queryset.filter(scope_type=scope_type)
        if period_type:
            queryset = queryset.filter(period_type=period_type)
        return queryset
