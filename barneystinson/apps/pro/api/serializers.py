from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from ..models import Pro


class ProSerializer(serializers.ModelSerializer):
    logo = Base64ImageField(required=False, default=Pro.DEFAULT_LOGO)

    class Meta:
        model = Pro
        exclude = ('is_active', )
