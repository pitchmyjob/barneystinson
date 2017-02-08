from rest_framework import serializers

from django.utils.translation import ugettext as _

from apps.authentication.api.serializers import UserSerializer

from ..models import CandidacyMessage


class CandidacyMessageSerializer(serializers.ModelSerializer):
    emmiter = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    emmiter_extra = UserSerializer(source='emmiter', read_only=True)

    class Meta:
        model = CandidacyMessage
        fields = ('id', 'candidacy', 'emmiter', 'emmiter_extra', 'message', 'created')
        read_only_fields = ('id', 'created')

    def validate_candidacy(self, value):
        request = self.context.get('request')
        if request.user.is_pro and value.job.pro != request.user.pro:
            raise serializers.ValidationError(_('La candidature ne correspond pas à une offre de votre structure'))
        elif request.user.is_applicant and value.applicant != request.user.applicant:
            raise serializers.ValidationError(_('La candidature ne vous est pas liée'))
        return value

    def update(self, instance, validated_data):
        del validated_data['candidacy']
        return super(CandidacyMessageSerializer, self).update(instance, validated_data)
