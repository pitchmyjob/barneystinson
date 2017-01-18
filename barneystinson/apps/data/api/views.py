from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ..models import Industry, Employee, ContractType, Experience, StudyLevel
from .serializers import (IndustrySerializer, EmployeeSerializer, ContractTypeSerializer, ExperienceSerializer,
                          StudyLevelSerializer)


class IndustryViewSet(ListModelMixin, GenericViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class EmployeeViewSet(ListModelMixin, GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ContractTypeViewSet(ListModelMixin, GenericViewSet):
    queryset = ContractType.objects.all()
    serializer_class = ContractTypeSerializer


class ExperienceViewSet(ListModelMixin, GenericViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class StudyLevelViewSet(ListModelMixin, GenericViewSet):
    queryset = StudyLevel.objects.all()
    serializer_class = StudyLevelSerializer
