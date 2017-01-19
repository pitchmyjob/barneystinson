from rest_framework.viewsets import ModelViewSet

from apps.core.api.mixins import IsAuthenticatedMixin, IsActiveDestroyMixin

from ..models import Job, JobQuestion
from .filters import JobFilter
from .serializers import JobSerializer, JobQuestionSerializer


class JobViewSet(IsAuthenticatedMixin, IsActiveDestroyMixin, ModelViewSet):
    serializer_class = JobSerializer
    filter_class = JobFilter
    search_fields = ('title', 'description')

    def get_queryset(self):
        pro = self.request.user.pro
        if pro:
            qs = Job.objects.prefetch_related('contract_types', 'experiences', 'study_levels')
            return qs.filter(pro=pro, is_active=True)
        return Job.objects.none()

    def perform_create(self, serializer):
        serializer.save(pro=self.request.user.pro)


class JobQuestionViewSet(IsAuthenticatedMixin, ModelViewSet):
    serializer_class = JobQuestionSerializer
    filter_fields = ('job',)

    def get_queryset(self):
        pro = self.request.user.pro
        if pro:
            return JobQuestion.objects.filter(job__pro=pro, job__is_active=True)
        return JobQuestion.objects.none()
