from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet

from apps.core.api.mixins import IsAuthenticatedMixin
from apps.event.mixins import EventApplicantMixin

from .permissions import IsApplicantUser
from .serializers import (ApplicantMeSerializer, ApplicantExperienceSerializer, ApplicantEducationSerializer,
                          ApplicantSkillSerializer, ApplicantLanguageSerializer, ApplicantInterestSerializer)
from ..models import ApplicantExperience, ApplicantEducation, ApplicantSkill, ApplicantLanguage, ApplicantInterest


class ApplicantMeAPIView(EventApplicantMixin, generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = ApplicantMeSerializer
    event_type = 'applicant'

    def get_object(self):
        return self.request.user.applicant


class ApplicantExperienceViewSet(EventApplicantMixin, IsAuthenticatedMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = ApplicantExperienceSerializer
    event_type = 'experience'

    def get_queryset(self):
        return ApplicantExperience.objects.filter(applicant__user=self.request.user)


class ApplicantEducationViewSet(EventApplicantMixin, IsAuthenticatedMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = ApplicantEducationSerializer
    event_type = 'education'

    def get_queryset(self):
        return ApplicantEducation.objects.filter(applicant__user=self.request.user)


class ApplicantSkillViewSet(EventApplicantMixin, IsAuthenticatedMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = ApplicantSkillSerializer
    event_type = 'skill'

    def get_queryset(self):
        return ApplicantSkill.objects.filter(applicant__user=self.request.user)


class ApplicantLanguageViewSet(EventApplicantMixin, IsAuthenticatedMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = ApplicantLanguageSerializer
    event_type = 'language'

    def get_queryset(self):
        return ApplicantLanguage.objects.filter(applicant__user=self.request.user)


class ApplicantInterestViewSet(EventApplicantMixin, IsAuthenticatedMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = ApplicantInterestSerializer
    event_type = 'interest'

    def get_queryset(self):
        return ApplicantInterest.objects.filter(applicant__user=self.request.user)
