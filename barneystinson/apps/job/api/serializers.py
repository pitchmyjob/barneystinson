from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from django.utils import timezone
from django.utils.translation import ugettext as _

from apps.pro.api.serializers import ProSerializer

from ..models import Job, JobQuestion


class ValidateJobSerializer(object):
    def validate_job(self, value):
        request = self.context.get('request')
        if value.pro != request.user.pro:
            raise serializers.ValidationError(_('L\'identifiant ne correspond pas à votre structure'))
        return value


class JobSerializer(serializers.ModelSerializer):
    logo = Base64ImageField(source='pro.logo', required=False)
    state = serializers.SerializerMethodField()
    contract_types_extra = serializers.StringRelatedField(source='contract_types', many=True, read_only=True)
    experiences_extra = serializers.StringRelatedField(source='experiences', many=True, read_only=True)
    study_levels_extra = serializers.StringRelatedField(source='study_levels', many=True, read_only=True)
    candidacy_count = serializers.ReadOnlyField(source='candidacy_set.count')

    class Meta:
        model = Job
        exclude = ('is_active',)
        read_only_fields = ('id', 'pro', 'last_payment', 'request_credits', 'view_counter')

    def get_state(self, obj):
        return {
            'code': obj.get_state_code(),
            'label': obj.get_state(),
        }

    def create(self, validated_data):
        request = self.context.get('request')

        pro = validated_data.pop('pro', None)
        if pro:
            logo = pro.get('logo')
            if logo:
                request.user.pro.logo = logo
                request.user.pro.save()

        validated_data['pro'] = request.user.pro
        job = super(JobSerializer, self).create(validated_data)
        JobQuestion.objects.create(job=job)  # TODO: remove this line to deal with multiple question
        return job

    def update(self, instance, validated_data):
        request = self.context.get('request')

        pro = validated_data.pop('pro', None)
        if pro:
            logo = pro.get('logo')
            if logo:
                request.user.pro.logo = logo
                request.user.pro.save()
        return super(JobSerializer, self).update(instance, validated_data)


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
