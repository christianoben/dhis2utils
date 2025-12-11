from rest_framework import viewsets, permissions
from .models import Pool
from .serializers import PoolSerializer


class PoolViewSet(viewsets.ModelViewSet):
    queryset = Pool.objects.select_related('ward__sub_county__county', 'owner')
    serializer_class = PoolSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
