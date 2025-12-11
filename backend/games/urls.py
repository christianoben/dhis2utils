from rest_framework.routers import DefaultRouter
from .views import GameViewSet

router = DefaultRouter()
router.register(r'', GameViewSet)

urlpatterns = router.urls
