from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet

from apps.core.api.mixins import IsAuthenticatedMixin

from .permissions import IsApplicantUser
from .serializers import (ApplicantMeSerializer, ApplicantExperienceSerializer, ApplicantEducationSerializer,
                          ApplicantSkillSerializer, ApplicantLanguageSerializer, ApplicantInterestSerializer)
from ..models import ApplicantExperience, ApplicantEducation, ApplicantSkill, ApplicantLanguage, ApplicantInterest


class ApplicantMeAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = ApplicantMeSerializer

    def get_object(self):
        return self.request.user.applicant


class ApplicantExperienceViewSet(IsAuthenticatedMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = ApplicantExperienceSerializer

    def get_queryset(self):
        return ApplicantExperience.objects.filter(applicant__user=self.request.user)


class ApplicantEducationViewSet(IsAuthenticatedMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = ApplicantEducationSerializer

    def get_queryset(self):
        return ApplicantEducation.objects.filter(applicant__user=self.request.user)


class ApplicantSkillViewSet(IsAuthenticatedMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = ApplicantSkillSerializer

    def get_queryset(self):
        return ApplicantSkill.objects.filter(applicant__user=self.request.user)


class ApplicantLanguageViewSet(IsAuthenticatedMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = ApplicantLanguageSerializer

    def get_queryset(self):
        return ApplicantLanguage.objects.filter(applicant__user=self.request.user)


class ApplicantInterestViewSet(IsAuthenticatedMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = ApplicantInterestSerializer

    def get_queryset(self):
        return ApplicantInterest.objects.filter(applicant__user=self.request.user)
