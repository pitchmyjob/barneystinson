from django.conf.urls import url

from .views import (AuthRegisterApplicantAPIView, AuthLoginApplicantAPIView, AuthRegisterProAPIView,
                    AuthLoginProAPIView, AuthMeAPIView, ForgetPasswordRequestAPIView,
                    ForgetPasswordConfirmAPIView, ChangePasswordAPIView,
                    AuthRegisterConfirmApplicantAPIView, AuthRegisterConfirmProAPIView, EmailExistsAPIView)


urlpatterns = [
    url(r'^auth/applicant/register', AuthRegisterApplicantAPIView.as_view(), name='applicant-register'),
    url(r'^auth/applicant/login', AuthLoginApplicantAPIView.as_view(), name='applicant-login'),
    url(r'^auth/applicant/confirm', AuthRegisterConfirmApplicantAPIView.as_view(), name='applicant-register-confirm'),
    url(r'^auth/pro/register', AuthRegisterProAPIView.as_view(), name='pro-register'),
    url(r'^auth/pro/login', AuthLoginProAPIView.as_view(), name='pro-login'),
    url(r'^auth/pro/confirm', AuthRegisterConfirmProAPIView.as_view(), name='pro-register-confirm'),
    url(r'^auth/forget-password-request', ForgetPasswordRequestAPIView.as_view(), name='forst-password-request'),
    url(r'^auth/forget-password-confirm', ForgetPasswordConfirmAPIView.as_view(), name='forst-password-confirm'),
    url(r'^auth/me/change-password', ChangePasswordAPIView.as_view(), name='me-change-password'),
    url(r'^auth/me', AuthMeAPIView.as_view(), name='me'),
    url(r'^auth/email-exists', EmailExistsAPIView.as_view(), name='email-exists'),
]
