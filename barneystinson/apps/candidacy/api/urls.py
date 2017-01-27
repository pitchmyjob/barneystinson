from django.conf.urls import url

from .views import (CandidacyProListAPIView, CandidacyProRetrieveAPIView, CandidacyProRequestAPIView,
                    CandidacyProApproveAPIView, CandidacyProDisapproveAPIView, CandidacyApplicantListAPIView,
                    CandidacyApplicantRetrieveAPIView, CandidacyApplicantLikeAPIView,
                    CandidacyApplicantPostulateAPIView)


urlpatterns = [
    url(r'^procandidacies/(?P<pk>\d+)/list', CandidacyProListAPIView.as_view(), name='procandidacy-detail'),
    url(r'^procandidacies/(?P<pk>\d+)/approve', CandidacyProApproveAPIView.as_view(), name='procandidacy-approve'),
    url(r'^procandidacies/(?P<pk>\d+)', CandidacyProRetrieveAPIView.as_view(), name='procandidacy-detail'),
    url(r'^procandidacies/request', CandidacyProRequestAPIView.as_view(), name='procandidacy-request'),
    url(
        r'^procandidacies/(?P<pk>\d+)/disapprove',
        CandidacyProDisapproveAPIView.as_view(),
        name='procandidacy-disapprove'
    ),
    url(
        r'^applicantcandidacies/(?P<pk>\d+)/like',
        CandidacyApplicantLikeAPIView.as_view(),
        name='applicantcandidacy-like'
    ),
    url(
        r'^applicantcandidacies/(?P<pk>\d+)/postulate',
        CandidacyApplicantPostulateAPIView.as_view(),
        name='applicantcandidacy-postulate'
    ),
    url(
        r'^applicantcandidacies/(?P<pk>\d+)',
        CandidacyApplicantRetrieveAPIView.as_view(),
        name='applicantcandidacy-detail'
    ),
    url(r'^applicantcandidacies', CandidacyApplicantListAPIView.as_view(), name='applicantcandidacy-detail'),
]
