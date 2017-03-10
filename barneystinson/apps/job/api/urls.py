from rest_framework.routers import SimpleRouter

from django.conf.urls import url

from .views import JobViewSet, JobQuestionViewSet, JobMatchingApiView



router = SimpleRouter()
router.register('jobs', JobViewSet, base_name='job')
router.register('jobquestions', JobQuestionViewSet, base_name='jobquestion')


urlpatterns = router.urls + [
    url(r'^jobs/matching/', JobMatchingApiView.as_view(), name='job-matching'),
]