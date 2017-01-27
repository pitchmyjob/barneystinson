from django.conf.urls import url

from .views import (AuthRegisterApplicantAPIView, AuthLoginApplicantAPIView, AuthRegisterProAPIView,
                    AuthLoginProAPIView, AuthMeAPIView)


urlpatterns = [
    url(r'^auth/applicant/register', AuthRegisterApplicantAPIView.as_view(), name='applicant-register'),
    url(r'^auth/applicant/login', AuthLoginApplicantAPIView.as_view(), name='applicant-login'),
    url(r'^auth/pro/register', AuthRegisterProAPIView.as_view(), name='pro-register'),
    url(r'^auth/pro/login', AuthLoginProAPIView.as_view(), name='pro-login'),
    url(r'^auth/me', AuthMeAPIView.as_view(), name='me'),
]
