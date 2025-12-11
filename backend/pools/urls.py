from rest_framework.routers import DefaultRouter
from .views import PoolViewSet

router = DefaultRouter()
router.register(r'', PoolViewSet)

urlpatterns = router.urls
