from rest_framework.routers import DefaultRouter

from .views import JobViewSet, JobQuestionViewSet


router = DefaultRouter()
router.register('jobs', JobViewSet, base_name='job')
router.register('jobquestions', JobQuestionViewSet, base_name='jobquestion')
