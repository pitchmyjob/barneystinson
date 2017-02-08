from rest_framework.routers import SimpleRouter

from .views import CandidacyMessageViewSet


router = SimpleRouter()
router.register('messages', CandidacyMessageViewSet, base_name='message')

urlpatterns = router.urls
