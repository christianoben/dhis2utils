from rest_framework import serializers
from .models import RecommendedMatch


class RecommendedMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedMatch
        fields = [
            'id', 'pool', 'player1', 'player2', 'reason', 'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
