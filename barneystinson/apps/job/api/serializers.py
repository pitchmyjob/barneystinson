from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from django.utils import timezone
from django.utils.translation import ugettext as _

from apps.pro.api.fields import CurrentProDefault
from apps.pro.api.serializers import ProSerializer
from apps.pro.models import Pro

from ..models import Job, JobQuestion


class ValidateJobSerializer(object):
    def validate_job(self, value):
        request = self.context.get('request')
        if value.pro != request.user.pro:
            raise serializers.ValidationError(_('L\'identifiant ne correspond pas à votre structure'))
        return value


class JobSerializer(serializers.ModelSerializer):
    logo = Base64ImageField(source='pro.logo', default=Pro.DEFAULT_LOGO)
    pro = serializers.PrimaryKeyRelatedField(read_only=True, default=CurrentProDefault())
    state = serializers.SerializerMethodField()
    contract_types_extra = serializers.StringRelatedField(source='contract_types', many=True, read_only=True)
    experiences_extra = serializers.StringRelatedField(source='experiences', many=True, read_only=True)
    study_levels_extra = serializers.StringRelatedField(source='study_levels', many=True, read_only=True)

    class Meta:
        model = Job
        exclude = ('is_active',)
        read_only_fields = ('id', 'last_payment', 'request_credits', 'view_counter')

    def get_state(self, obj):
        return obj.get_state()


class JobQuestionSerializer(ValidateJobSerializer, serializers.ModelSerializer):
    class Meta:
        model = JobQuestion
        fields = '__all__'


class JobFullSerializer(serializers.ModelSerializer):
    pro = ProSerializer()

    class Meta:
        model = Job
        fields = '__all__'


class JobPublishSerializer(ValidateJobSerializer, serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'last_payment')
        read_only_fields = ('last_payment',)

    def update(self, instance, validated_data):
        validated_data['last_payment'] = timezone.now()
        return super(JobPublishSerializer, self).update(instance, validated_data)
