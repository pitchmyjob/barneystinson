from rest_framework import serializers

from django.utils.translation import ugettext as _

from apps.pro.api.fields import CurrentProDefault
from apps.pro.api.serializers import ProSerializer

from ..models import Job, JobQuestion


class JobSerializer(serializers.ModelSerializer):
    pro = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentProDefault())

    class Meta:
        model = Job
        fields = '__all__'


class JobQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobQuestion
        fields = '__all__'

    def validate_job(self, value):
        request = self.context.get('request')
        if value.pro != request.user.pro:
            raise serializers.ValidationError(_('L\'identifiant ne correspond pas à votre structure'))
        return value


class JobFullSerializer(serializers.ModelSerializer):
    pro = ProSerializer()

    class Meta:
        model = Job
        fields = '__all__'
