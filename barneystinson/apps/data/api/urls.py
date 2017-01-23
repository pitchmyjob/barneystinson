from rest_framework.routers import DefaultRouter

from .views import IndustryViewSet, EmployeeViewSet, ContractTypeViewSet, ExperienceViewSet, StudyLevelViewSet


router = DefaultRouter()
router.register('industries', IndustryViewSet)
router.register('employees', EmployeeViewSet)
router.register('contracttypes', ContractTypeViewSet)
router.register('experiences', ExperienceViewSet)
router.register('studylevels', StudyLevelViewSet)

urlpatterns = router.urls
