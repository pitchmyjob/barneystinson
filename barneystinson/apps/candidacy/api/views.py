from rest_framework import generics, permissions, status
from rest_framework.response import Response

from django.db.models import F, Q

from apps.job.models import Job
from apps.applicant.api.permissions import IsApplicantUser
from apps.pro.api.permissions import IsProUser

from ..models import Candidacy
from .serializers import (CandidacyProReadSerializer, CandidacyProRequestSerializer, CandidacyProApproveSerializer,
                          CandidacyProDisapproveSerializer, CandidacyApplicantReadSerializer,
                          CandidacyApplicantLikeSerializer, CandidacyApplicantVideoSerializer)


class CandidacyProListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = CandidacyProReadSerializer

    def get_queryset(self):
        qs_filter = {'job': self.kwargs[self.lookup_field]}
        return Candidacy.objects.filter(~Q(status=Candidacy.MATCHING), job__pro=self.request.user.pro, **qs_filter)


class CandidacyProRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = CandidacyProReadSerializer

    def get_queryset(self):
        return Candidacy.objects.filter(~Q(status=Candidacy.MATCHING), job__pro=self.request.user.pro)


class CandidacyProRequestAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = CandidacyProRequestSerializer

    def post(self, request):
        job = request.data.get('job')
        applicant = request.data.get('applicant')

        candidacy = Candidacy.objects.filter(job=job, applicant=applicant).first()
        if candidacy:
            serializer = self.get_serializer(candidacy, data=request.data)
            serializer.is_valid(raise_exception=True)
            if candidacy.is_matching:
                Job.objects.filter(pk=job).update(request_credits=F('request_credits') - 1)
            serializer.save()
            return Response(serializer.data)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CandidacyProApproveAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = CandidacyProApproveSerializer

    def get_queryset(self):
        return Candidacy.objects.filter(~Q(status=Candidacy.MATCHING), job__pro=self.request.user.pro)


class CandidacyProDisapproveAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = CandidacyProDisapproveSerializer

    def get_queryset(self):
        return Candidacy.objects.filter(~Q(status=Candidacy.MATCHING), job__pro=self.request.user.pro)


class CandidacyApplicantListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = CandidacyApplicantReadSerializer

    def get_queryset(self):
        return Candidacy.objects.filter(applicant=self.request.user.applicant)


class CandidacyApplicantRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = CandidacyApplicantReadSerializer

    def get_queryset(self):
        return Candidacy.objects.filter(applicant=self.request.user.applicant)


class CandidacyApplicantLikeAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = CandidacyApplicantLikeSerializer

    def get_queryset(self):
        return Candidacy.objects.filter(applicant=self.request.user.applicant)


class CandidacyApplicantPostulateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsApplicantUser]
    serializer_class = CandidacyApplicantVideoSerializer

    def get_queryset(self):
        return Candidacy.objects.filter(applicant=self.request.user.applicant)
