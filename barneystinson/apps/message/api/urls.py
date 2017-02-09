from rest_framework.routers import SimpleRouter

from django.conf.urls import url

from .views import CandidacyMessageViewSet, CandidacyMessageJobListAPIView


router = SimpleRouter()
router.register('messages', CandidacyMessageViewSet, base_name='message')

urlpatterns = router.urls + [
    url(r'^messages/job/(?P<pk>\d+)', CandidacyMessageJobListAPIView.as_view(), name='message-job-list'),
]
