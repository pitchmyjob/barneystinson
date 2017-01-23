from rest_framework import serializers

from ..models import Pro


class ProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pro
        fields = '__all__'
