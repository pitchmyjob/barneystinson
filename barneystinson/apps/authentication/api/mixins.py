from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext as _


class AuthLoginMixin(object):
    login_type = None

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

    def get_serializer_context(self):
        if not self.login_type:
            raise ImproperlyConfigured(_('"login_type" attribute must be defined'))
        return {'login_type': self.login_type}
