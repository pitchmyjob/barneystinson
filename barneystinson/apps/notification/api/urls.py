from rest_framework.routers import SimpleRouter

from .views import NotificationViewSet


router = SimpleRouter()
router.register('notifications', NotificationViewSet, base_name='notification')

urlpatterns = router.urls
