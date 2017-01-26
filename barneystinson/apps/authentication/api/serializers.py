from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _

from apps.applicant.models import Applicant
from apps.pro.models import Pro

from ..models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source='auth_token.key', read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'token']
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }


class UserRegisterApplicantSerializer(UserRegisterSerializer):
    photo = Base64ImageField(required=False, default=User.DEFAULT_PHOTO)

    class Meta(UserRegisterSerializer.Meta):
        fields = UserRegisterSerializer.Meta.fields + ['photo']

    def create(self, validated_data):
        photo = validated_data.pop('photo', None)
        user = User.objects.create_user(username=validated_data['email'], **validated_data)
        user.photo = photo
        user.save()
        Applicant.objects.create(user=user)
        return user


class UserRegisterProSerializer(UserRegisterSerializer):
    logo = Base64ImageField(source='pro.logo', required=False, default=Pro.DEFAULT_LOGO)
    company = serializers.CharField(source='pro.company')

    class Meta(UserRegisterSerializer.Meta):
        fields = UserRegisterSerializer.Meta.fields + ['logo', 'company']

    def create(self, validated_data):
        logo = validated_data['pro'].pop('logo', None)
        pro = Pro.objects.create(company=validated_data['pro']['company'])
        pro.logo = logo
        pro.save()
        validated_data['pro'] = pro
        return super(UserRegisterProSerializer, self).create(validated_data)


class AutLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        login_type = self.context.get('login_type')

        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg, code='authorization')
                elif login_type == 'applicant' and not hasattr(user, 'applicant'):
                    msg = _('User account isn\'t linked to a applicant')
                    raise serializers.ValidationError(msg, code='authorization')
                elif login_type == 'pro' and not user.pro:
                    msg = _('User account isn\'t linked to a company')
                    raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
