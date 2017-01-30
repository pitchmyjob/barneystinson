from rest_framework import generics, status, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from django.db.models import F

from apps.job.models import Job

from .mixins import CandidacyProMixin, CandidacyApplicantMixin, CandidacyProPermissionMixin
from .serializers import CandidacyProCommentSerializer
from ..models import Candidacy, CandidacyComment


class CandidacyProListAPIView(CandidacyProMixin, generics.ListAPIView):
    pass


class CandidacyProRetrieveAPIView(CandidacyProMixin, generics.RetrieveAPIView):
    pass


class CandidacyProRequestAPIView(CandidacyProMixin, generics.GenericAPIView):
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


class CandidacyProApproveAPIView(CandidacyProMixin, generics.UpdateAPIView):
    pass


class CandidacyProDisapproveAPIView(CandidacyProMixin, generics.UpdateAPIView):
    pass


class CandidacyApplicantListAPIView(CandidacyApplicantMixin, generics.ListAPIView):
    pass


class CandidacyApplicantRetrieveAPIView(CandidacyApplicantMixin, generics.RetrieveAPIView):
    pass


class CandidacyApplicantLikeAPIView(CandidacyApplicantMixin, generics.UpdateAPIView):
    pass


class CandidacyApplicantPostulateAPIView(CandidacyApplicantMixin, generics.UpdateAPIView):
    pass


class CandidacyProCommentViewSet(CandidacyProPermissionMixin,
                                 mixins.ListModelMixin,
                                 mixins.CreateModelMixin,
                                 mixins.DestroyModelMixin,
                                 GenericViewSet):
    serializer_class = CandidacyProCommentSerializer
    filter_fields = ('candidacy',)

    def get_queryset(self):
        return CandidacyComment.objects.filter(candidacy__job__pro=self.request.user.pro)
