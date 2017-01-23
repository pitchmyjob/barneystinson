from rest_framework.routers import SimpleRouter

from .views import IndustryViewSet, EmployeeViewSet, ContractTypeViewSet, ExperienceViewSet, StudyLevelViewSet


router = SimpleRouter()
router.register('industries', IndustryViewSet)
router.register('employees', EmployeeViewSet)
router.register('contracttypes', ContractTypeViewSet)
router.register('experiences', ExperienceViewSet)
router.register('studylevels', StudyLevelViewSet)

urlpatterns = router.urls
