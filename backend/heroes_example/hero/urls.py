from rest_framework.routers import DefaultRouter

from .viewsets import HeroViewSet

router = DefaultRouter()
router.register('heroes', HeroViewSet)

urlpatterns = router.urls
