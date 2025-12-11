from rest_framework import serializers
from .models import County, SubCounty, Ward


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ['id', 'name']


class SubCountySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCounty
        fields = ['id', 'name', 'county']


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ['id', 'name', 'sub_county', 'created_at']
        read_only_fields = ['created_at']
