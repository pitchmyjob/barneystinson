from rest_framework import serializers

from apps.authentication.api.serializers import UserRegisterSerializer

from ..models import Pro


class ProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pro
        fields = '__all__'


class ProRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pro
        fields = ('company',)


class ProRegisterSerializer(serializers.Serializer):
    pro = ProRegisterSerializer()
    user = UserRegisterSerializer()
