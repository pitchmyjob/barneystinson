from apps.core.api import tests

from .serializers import (IndustrySerializer, EmployeeSerializer, ContractTypeSerializer, ExperienceSerializer,
                          StudyLevelSerializer)
from ..factories import IndustryFactory, EmployeeFactory, ContractTypeFactory, ExperienceFactory, StudyLevelFactory


class IndustryAPITestCase(tests.ListAPITestCaseMixin, tests.BaseAPITestCase):
    base_name = 'industry'
    factory_class = IndustryFactory
    serializer_class = IndustrySerializer


class EmployeeAPITestCase(tests.ListAPITestCaseMixin, tests.BaseAPITestCase):
    base_name = 'employee'
    factory_class = EmployeeFactory
    serializer_class = EmployeeSerializer


class ContractTypeAPITestCase(tests.ListAPITestCaseMixin, tests.BaseAPITestCase):
    base_name = 'contracttype'
    factory_class = ContractTypeFactory
    serializer_class = ContractTypeSerializer


class ExperienceAPITestCase(tests.ListAPITestCaseMixin, tests.BaseAPITestCase):
    base_name = 'experience'
    factory_class = ExperienceFactory
    serializer_class = ExperienceSerializer


class StudyLevelAPITestCase(tests.ListAPITestCaseMixin, tests.BaseAPITestCase):
    base_name = 'studylevel'
    factory_class = StudyLevelFactory
    serializer_class = StudyLevelSerializer
