from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from apps.core.api.mixins import IsActiveDestroyMixin
from apps.pro.api.permissions import IsProUser

from ..models import Job, JobQuestion
from .filters import JobFilter
from .serializers import JobSerializer, JobQuestionSerializer


class JobViewSet(IsActiveDestroyMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = JobSerializer
    filter_class = JobFilter
    search_fields = ('title', 'description')

    def get_queryset(self):
        qs = Job.objects.prefetch_related('contract_types', 'experiences', 'study_levels')
        return qs.filter(pro=self.request.user.pro, is_active=True)


class JobQuestionViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = JobQuestionSerializer
    filter_fields = ('job',)

    def get_queryset(self):
        JobQuestion.objects.filter(job__pro=self.request.user.pro, job__is_active=True)
