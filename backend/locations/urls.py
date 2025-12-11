from rest_framework.routers import DefaultRouter
from .views import CountyViewSet, SubCountyViewSet, WardViewSet

router = DefaultRouter()
router.register(r'counties', CountyViewSet)
router.register(r'sub-counties', SubCountyViewSet)
router.register(r'wards', WardViewSet)

urlpatterns = router.urls
