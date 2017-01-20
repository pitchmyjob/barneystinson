from rest_framework import mixins
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.authentication.models import User
from apps.core.api.mixins import IsAuthenticatedMixin

from ..models import Applicant, Experience, Formation, Skill, Language, Interest
from .serializers import (ApplicantSerializer, ExperienceSerializer, FormationSerializer, SkillSerializer,
                          LanguageSerializer, InterestSerializer)


class ApplicantViewSet(IsAuthenticatedMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       GenericViewSet):
    serializer_class = ApplicantSerializer

    def get_queryset(self):
        return Applicant.objects.filter(user=self.request.user)


class ExperienceViewSet(IsAuthenticatedMixin, ModelViewSet):
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        return Experience.objects.filter(applicant__user=self.request.user)


class FormationViewSet(IsAuthenticatedMixin, ModelViewSet):
    serializer_class = FormationSerializer

    def get_queryset(self):
        return Formation.objects.filter(applicant__user=self.request.user)


class SkillViewSet(IsAuthenticatedMixin, ModelViewSet):
    serializer_class = SkillSerializer

    def get_queryset(self):
        return Skill.objects.filter(applicant__user=self.request.user)


class LanguageViewSet(IsAuthenticatedMixin, ModelViewSet):
    serializer_class = LanguageSerializer

    def get_queryset(self):
        return Language.objects.filter(applicant__user=self.request.user)


class InterestViewSet(IsAuthenticatedMixin, ModelViewSet):
    serializer_class = InterestSerializer

    def get_queryset(self):
        return Interest.objects.filter(applicant__user=self.request.user)
