from rest_framework.routers import DefaultRouter
from .views import RecommendedMatchViewSet

router = DefaultRouter()
router.register(r'', RecommendedMatchViewSet)

urlpatterns = router.urls
