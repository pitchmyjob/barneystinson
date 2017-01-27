from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from apps.authentication.models import User

from ..models import (Applicant, ApplicantExperience, ApplicantEducation, ApplicantSkill, ApplicantLanguage,
                      ApplicantInterest)
from .fields import CurrentApplicantDefault


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


class ApplicantSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    photo = Base64ImageField(source='user.photo', read_only=True, default=User.DEFAULT_PHOTO)
    experiences = ApplicantExperienceSerializer(many=True, read_only=True)
    educations = ApplicantEducationSerializer(many=True, read_only=True)
    skills = ApplicantSkillSerializer(many=True, read_only=True)
    languages = ApplicantLanguageSerializer(many=True, read_only=True)
    interests = ApplicantInterestSerializer(many=True, read_only=True)

    class Meta:
        model = Applicant
        fields = '__all__'


class ApplicantMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        exclude = ('user',)
