from rest_framework import viewsets, permissions
from .models import County, SubCounty, Ward
from .serializers import CountySerializer, SubCountySerializer, WardSerializer


class CountyViewSet(viewsets.ModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer
    permission_classes = [permissions.IsAuthenticated]


class SubCountyViewSet(viewsets.ModelViewSet):
    queryset = SubCounty.objects.select_related('county')
    serializer_class = SubCountySerializer
    permission_classes = [permissions.IsAuthenticated]


class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.select_related('sub_county__county')
    serializer_class = WardSerializer
    permission_classes = [permissions.IsAuthenticated]
