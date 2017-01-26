from rest_framework import serializers

from django.utils import timezone
from django.utils.translation import ugettext as _

from apps.applicant.api.serializers import ApplicantSerializer

from ..models import Candidacy


class CandidacyProReadSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer()

    class Meta:
        model = Candidacy
        fields = ('applicant', 'status', 'date_matching', 'date_like', 'date_request', 'date_video', 'date_decision')
        depth = 1


class CandidacyActionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidacy
        fields = ('job', 'applicant', 'status')
        read_only_fields = ('status',)

    def validate_job(self, value):
        request = self.context.get('request')
        if value.pro != request.user.pro:
            raise serializers.ValidationError(_('L\'identifiant ne correspond pas à votre structure'))
        return value


class CandidacyProRequestSerializer(CandidacyActionRequestSerializer):
    def update_validated_data(self, validated_data):
        request = self.context.get('request')
        validated_data.update({
            'collaborator': request.user,
            'status': Candidacy.REQUEST,
            'date_request': timezone.now(),
        })
        return validated_data

    def create(self, validated_data):
        validated_data = self.update_validated_data(validated_data)
        return super(CandidacyProRequestSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data = self.update_validated_data(validated_data)
        return super(CandidacyProRequestSerializer, self).update(instance, validated_data)


class CandidacyProApproveSerializer(CandidacyActionRequestSerializer):
    def update(self, instance, validated_data):
        validated_data.update({'status': Candidacy.SELECTED, 'date_decision': timezone.now()})
        return super(CandidacyProApproveSerializer, self).update(instance, validated_data)


class CandidacyProDisapproveSerializer(CandidacyActionRequestSerializer):
    def update(self, instance, validated_data):
        validated_data.update({'status': Candidacy.NOT_SELECTED, 'date_decision': timezone.now()})
        return super(CandidacyProDisapproveSerializer, self).update(instance, validated_data)
