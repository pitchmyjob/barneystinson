from rest_framework.routers import DefaultRouter

from django.conf.urls import url

from .views import (ApplicantViewSet, ExperienceViewSet, FormationViewSet, SkillViewSet, LanguageViewSet,
                    InterestViewSet)


router = DefaultRouter()
router.register('applicants', ApplicantViewSet, base_name='applicant')
router.register('experiences', ExperienceViewSet, base_name='experience')
router.register('formations', FormationViewSet, base_name='formation')
router.register('skills', SkillViewSet, base_name='skill')
router.register('languages', LanguageViewSet, base_name='language')
router.register('interests', InterestViewSet, base_name='interest')

urlpatterns = router.urls
