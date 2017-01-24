from rest_framework import serializers

from ..models import (Applicant, ApplicantExperience, ApplicantEducation, ApplicantSkill, ApplicantLanguage,
                      ApplicantInterest)
from .fields import CurrentApplicantDefault


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'


class ApplicantExperienceSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentApplicantDefault())

    class Meta:
        model = ApplicantExperience
        fields = '__all__'


class ApplicantEducationSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentApplicantDefault())

    class Meta:
        model = ApplicantEducation
        fields = '__all__'


class ApplicantSkillSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentApplicantDefault())

    class Meta:
        model = ApplicantSkill
        fields = '__all__'


class ApplicantLanguageSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentApplicantDefault())

    class Meta:
        model = ApplicantLanguage
        fields = '__all__'


class ApplicantInterestSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentApplicantDefault())

    class Meta:
        model = ApplicantInterest
        fields = '__all__'
