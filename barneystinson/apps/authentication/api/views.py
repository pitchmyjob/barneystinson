from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from .mixins import AuthLoginMixin
from .serializers import UserRegisterApplicantSerializer, UserRegisterProSerializer, AutLoginSerializer


class AuthRegisterApplicantAPIView(CreateAPIView):
    serializer_class = UserRegisterApplicantSerializer


class AuthLoginApplicantAPIView(AuthLoginMixin, APIView):
    serializer_class = AutLoginSerializer
    login_type = 'applicant'


class AuthRegisterProAPIView(CreateAPIView):
    serializer_class = UserRegisterProSerializer


class AuthLoginProAPIView(AuthLoginMixin, APIView):
    serializer_class = AutLoginSerializer
    login_type = 'pro'
