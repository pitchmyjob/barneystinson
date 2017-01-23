from rest_framework.routers import SimpleRouter

from .views import ProViewSet


router = SimpleRouter()
router.register('pros', ProViewSet, base_name='pro')

urlpatterns = router.urls
