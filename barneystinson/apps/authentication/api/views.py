from rest_framework import generics, permissions

from .mixins import AuthLoginMixin
from apps.event.mixins import EventApplicantMixin
from .serializers import UserRegisterApplicantSerializer, UserRegisterProSerializer, AutLoginSerializer, UserSerializer


class AuthRegisterApplicantAPIView(EventApplicantMixin, generics.CreateAPIView):
    serializer_class = UserRegisterApplicantSerializer
    event_type = "applicant"


class AuthLoginApplicantAPIView(AuthLoginMixin, generics.GenericAPIView):
    serializer_class = AutLoginSerializer
    login_type = 'applicant'


class AuthRegisterProAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterProSerializer


class AuthLoginProAPIView(AuthLoginMixin, generics.GenericAPIView):
    serializer_class = AutLoginSerializer
    login_type = 'pro'


class AuthMeAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
