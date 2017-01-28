from rest_framework import serializers

from django.utils import timezone

from apps.applicant.api.serializers import ApplicantFullSerializer
from apps.job.api.serializers import JobFullSerializer, ValidateJobSerializer

from ..models import Candidacy


class CandidacyProReadSerializer(serializers.ModelSerializer):
    applicant = ApplicantFullSerializer()

    class Meta:
        model = Candidacy
        fields = ('id', 'applicant', 'status', 'date_matching', 'date_like', 'date_request', 'date_video',
                  'date_decision')


class CandidacyProRequestSerializer(ValidateJobSerializer, serializers.ModelSerializer):
    class Meta:
        model = Candidacy
        fields = ('job', 'applicant', 'status')
        read_only_fields = ('status',)

    def get_validated_data(self, validated_data):
        validated_data.update({
            'collaborator': self.context.get('request').user,
            'status': Candidacy.REQUEST,
            'date_request': timezone.now(),
        })
        return validated_data

    def create(self, validated_data):
        return super(CandidacyProRequestSerializer, self).create(self.get_validated_data(validated_data))

    def update(self, instance, validated_data):
        return super(CandidacyProRequestSerializer, self).update(instance, self.get_validated_data(validated_data))


class CandidacyProActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidacy
        fields = ('job', 'applicant', 'status')
        read_only_fields = ('job', 'applicant', 'status')

    def update(self, instance, validated_data):
        return super(CandidacyProActionSerializer, self).update(instance, {
            'status': self.status_value,
            'date_decision': timezone.now()
        })


class CandidacyProApproveSerializer(CandidacyProActionSerializer):
    status_value = Candidacy.SELECTED


class CandidacyProDisapproveSerializer(CandidacyProActionSerializer):
    status_value = Candidacy.NOT_SELECTED


class CandidacyApplicantReadSerializer(serializers.ModelSerializer):
    job = JobFullSerializer()

    class Meta:
        model = Candidacy
        fields = ('id', 'job', 'status', 'date_matching', 'date_like', 'date_request', 'date_video', 'date_decision')


class CandidacyApplicantActionSerializer(CandidacyProActionSerializer):
    class Meta:
        model = Candidacy
        fields = ('job', 'applicant', 'status')
        read_only_fields = ('job', 'applicant', 'status')

    def update(self, instance, validated_data):
        return super(CandidacyApplicantActionSerializer, self).update(instance, {
            'status': self.status_value,
            self.date_field: timezone.now()
        })


class CandidacyApplicantLikeSerializer(CandidacyApplicantActionSerializer):
    status_value = Candidacy.LIKE
    date_field = 'date_like'


class CandidacyApplicantVideoSerializer(CandidacyApplicantActionSerializer):
    status_value = Candidacy.VIDEO
    date_field = 'date_video'
