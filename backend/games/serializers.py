from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id', 'pool', 'player1', 'player2', 'initiated_by', 'accepted_by', 'status',
            'start_time', 'end_time', 'winner', 'score_player1', 'score_player2',
            'result_submitted_by', 'result_confirmed_by', 'dispute_flag', 'dispute_notes',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
