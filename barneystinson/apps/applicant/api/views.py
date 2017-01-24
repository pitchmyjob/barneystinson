from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.core.api.mixins import IsAuthenticatedMixin

from ..models import (Applicant, ApplicantExperience, ApplicantEducation, ApplicantSkill, ApplicantLanguage,
                      ApplicantInterest)
from .serializers import (ApplicantSerializer, ApplicantExperienceSerializer, ApplicantEducationSerializer,
                          ApplicantSkillSerializer, ApplicantLanguageSerializer, ApplicantInterestSerializer)


class ApplicantViewSet(IsAuthenticatedMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       GenericViewSet):
    serializer_class = ApplicantSerializer

    def get_queryset(self):
        return Applicant.objects.filter(user=self.request.user)


class ApplicantExperienceViewSet(IsAuthenticatedMixin, ModelViewSet):
    serializer_class = ApplicantExperienceSerializer

    def get_queryset(self):
        return ApplicantExperience.objects.filter(applicant__user=self.request.user)


class ApplicantEducationViewSet(IsAuthenticatedMixin, ModelViewSet):
    serializer_class = ApplicantEducationSerializer

    def get_queryset(self):
        return ApplicantEducation.objects.filter(applicant__user=self.request.user)


class ApplicantSkillViewSet(IsAuthenticatedMixin, ModelViewSet):
    serializer_class = ApplicantSkillSerializer

    def get_queryset(self):
        return ApplicantSkill.objects.filter(applicant__user=self.request.user)


class ApplicantLanguageViewSet(IsAuthenticatedMixin, ModelViewSet):
    serializer_class = ApplicantLanguageSerializer

    def get_queryset(self):
        return ApplicantLanguage.objects.filter(applicant__user=self.request.user)


class ApplicantInterestViewSet(IsAuthenticatedMixin, ModelViewSet):
    serializer_class = ApplicantInterestSerializer

    def get_queryset(self):
        return ApplicantInterest.objects.filter(applicant__user=self.request.user)
