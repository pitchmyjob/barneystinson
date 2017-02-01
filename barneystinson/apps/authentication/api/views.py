from rest_framework import generics, permissions

from apps.core.utils import Email
from apps.event.mixins import EventApplicantMixin

from .mixins import AuthLoginMixin
from .serializers import UserRegisterApplicantSerializer, UserRegisterProSerializer, AutLoginSerializer, UserSerializer


class AuthRegisterApplicantAPIView(EventApplicantMixin, generics.CreateAPIView):
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


class AuthMeAPIView(EventApplicantMixin, generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    event_type = 'applicant'

    def get_object(self):
        return self.request.user
