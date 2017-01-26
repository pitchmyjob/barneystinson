from django.conf.urls import url

from .views import (CandidacyProListAPIView, CandidacyProRetrieveAPIView, CandidacyProRequestAPIView,
                    CandidacyProApproveAPIView, CandidacyProDisapproveAPIView)


urlpatterns = [
    url(r'^procandidacies/(?P<pk>\d+)/list', CandidacyProListAPIView.as_view(), name='procandidacy-detail'),
    url(r'^procandidacies/(?P<pk>\d+)', CandidacyProRetrieveAPIView.as_view(), name='procandidacy-detail'),
    url(r'^procandidacies/request', CandidacyProRequestAPIView.as_view(), name='procandidacy-request'),
    url(r'^procandidacies/(?P<pk>\d+)/approve', CandidacyProApproveAPIView.as_view(), name='procandidacy-approve'),
    url(
        r'^procandidacies/(?P<pk>\d+)/disapprove',
        CandidacyProDisapproveAPIView.as_view(),
        name='procandidacy-disapprove'
    ),
]
