from rest_framework import serializers
from .models import LeaderboardEntry


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderboardEntry
        fields = [
            'id', 'scope_type', 'scope_id', 'player', 'period_type', 'period_start',
            'period_end', 'wins', 'losses', 'games_played', 'rank', 'updated_at'
        ]
        read_only_fields = ['updated_at']
