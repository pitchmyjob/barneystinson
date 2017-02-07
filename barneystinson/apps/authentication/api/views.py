from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound

from django.shortcuts import get_object_or_404

from apps.core.utils import Email
from apps.event.mixins import EventApplicantViewSetMixin

from .mixins import AuthLoginMixin, AuthRegisterConfirmMixin
from .serializers import (UserRegisterApplicantSerializer, UserRegisterProSerializer, AutLoginSerializer,
                          UserSerializer, ForgetPasswordRequestSerializer, ForgetPasswordConfirmSerializer,
                          ChangePasswordSerializer, UserRegisterConfirmApplicantSerializer,
                          UserRegisterConfirmProSerializer)
from ..models import User


class AuthRegisterApplicantAPIView(EventApplicantViewSetMixin, generics.CreateAPIView):
    serializer_class = UserRegisterApplicantSerializer
    event_type = "applicant"

    def perform_create(self, serializer):
        super(AuthRegisterApplicantAPIView, self).perform_create(serializer)
        context = {'name': serializer.instance.get_full_name()}
        Email(subject='Inscription', to=serializer.instance, context=context,
              template='applicant/inscription.html').send()


class AuthLoginApplicantAPIView(AuthLoginMixin, generics.GenericAPIView):
    serializer_class = AutLoginSerializer
    login_type = 'applicant'


class AuthRegisterProAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterProSerializer

    def perform_create(self, serializer):
        super(AuthRegisterProAPIView, self).perform_create(serializer)
        context = {'name': serializer.instance.get_full_name()}
        Email(subject='Inscription', to=serializer.instance, context=context, template='pro/inscription.html').send()


class AuthLoginProAPIView(AuthLoginMixin, generics.GenericAPIView):
    serializer_class = AutLoginSerializer
    login_type = 'pro'


class AuthMeAPIView(EventApplicantViewSetMixin, generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    event_type = 'applicant'

    def get_object(self):
        return self.request.user


class ForgetPasswordRequestAPIView(generics.UpdateAPIView):
    serializer_class = ForgetPasswordRequestSerializer

    def get_object(self):
        email = self.request.data.get('email')
        if email:
            return get_object_or_404(User, email=email)
        raise NotFound()


class ForgetPasswordConfirmAPIView(generics.UpdateAPIView):
    serializer_class = ForgetPasswordConfirmSerializer

    def get_object(self):
        email = self.request.data.get('email')
        token = self.request.data.get('token')
        if email and token:
            return get_object_or_404(User, email=email, lost_password_token=token)
        raise NotFound()


class ChangePasswordAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user


class AuthRegisterConfirmApplicantAPIView(AuthRegisterConfirmMixin, generics.UpdateAPIView):
    serializer_class = UserRegisterConfirmApplicantSerializer
    token_field = 'confirm_phone_token'


class AuthRegisterConfirmProAPIView(AuthRegisterConfirmMixin, generics.UpdateAPIView):
    serializer_class = UserRegisterConfirmProSerializer
    token_field = 'confirm_email_token'
