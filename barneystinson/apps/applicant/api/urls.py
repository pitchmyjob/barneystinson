from rest_framework.routers import SimpleRouter

from .views import (ApplicantViewSet, ApplicantExperienceViewSet, ApplicantEducationViewSet, ApplicantSkillViewSet,
                    ApplicantLanguageViewSet, ApplicantInterestViewSet)


router = SimpleRouter()
router.register('applicants', ApplicantViewSet, base_name='applicant')
router.register('applicantexperiences', ApplicantExperienceViewSet, base_name='applicantexperience')
router.register('applicanteducations', ApplicantEducationViewSet, base_name='applicanteducation')
router.register('applicantskills', ApplicantSkillViewSet, base_name='applicantskill')
router.register('applicantlanguages', ApplicantLanguageViewSet, base_name='applicantlanguage')
router.register('applicantinterests', ApplicantInterestViewSet, base_name='applicantinterest')

urlpatterns = router.urls
