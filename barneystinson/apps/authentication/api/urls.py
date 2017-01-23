from django.conf.urls import url

from .views import AuthRegisterApplicantAPIView, AuthLoginApplicantAPIView, AuthRegisterProAPIView, AuthLoginProAPIView


urlpatterns = [
    url(r'^auth/applicant/register', AuthRegisterApplicantAPIView.as_view()),
    url(r'^auth/applicant/login', AuthLoginApplicantAPIView.as_view()),
    url(r'^auth/pro/register', AuthRegisterProAPIView.as_view()),
    url(r'^auth/pro/login', AuthLoginProAPIView.as_view()),
]
