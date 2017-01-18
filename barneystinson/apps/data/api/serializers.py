from rest_framework import serializers

from ..models import Industry, Employee, ContractType, Experience, StudyLevel


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ContractTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractType
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class StudyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyLevel
        fields = '__all__'
