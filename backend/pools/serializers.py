from rest_framework import serializers
from .models import Pool


class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = [
            'id', 'name', 'description', 'latitude', 'longitude', 'price_per_game',
            'ward', 'owner', 'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['status', 'created_at', 'updated_at']
