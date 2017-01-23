from rest_framework.routers import DefaultRouter

from .views import ProViewSet


router = DefaultRouter()
router.register('pros', ProViewSet, base_name='pro')

urlpatterns = router.urls
