from rest_framework import serializers

from ..models import Applicant, Experience, Formation, Skill, Language, Interest
from .fields import CurrentApplicantDefault


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentApplicantDefault())

    class Meta:
        model = Experience
        fields = '__all__'


class FormationSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentApplicantDefault())
    class Meta:
        model = Formation
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentApplicantDefault())
    class Meta:
        model = Skill
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentApplicantDefault())
    class Meta:
        model = Language
        fields = '__all__'


class InterestSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentApplicantDefault())
    class Meta:
        model = Interest
        fields = '__all__'
