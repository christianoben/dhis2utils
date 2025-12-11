from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PlayerViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'players', PlayerViewSet)

urlpatterns = router.urls
