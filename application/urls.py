from rest_framework.routers import DefaultRouter

from .views import ApplicationViewSet

router = DefaultRouter()
router.register(r'application', ApplicationViewSet)

urlpatterns = router.urls
