from rest_framework import decorators, permissions
from rest_framework.viewsets import ModelViewSet

from apps.core.api.mixins import IsActiveDestroyMixin
from apps.pro.api.permissions import IsProUser
from apps.event.mixins import EventJobMixin

from ..models import Job, JobQuestion
from .filters import JobFilter
from .serializers import JobSerializer, JobQuestionSerializer, JobPublishSerializer


class JobViewSet(IsActiveDestroyMixin, EventJobMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = JobSerializer
    filter_class = JobFilter
    search_fields = ('title', 'description')

    def get_queryset(self):
        qs = Job.objects.prefetch_related('contract_types', 'experiences', 'study_levels')
        return qs.filter(pro=self.request.user.pro, is_active=True)

    @decorators.list_route(methods=['put', 'patch'], serializer_class=JobPublishSerializer)
    def publish(self, request, pk=None):
        self.kwargs['pk'] = request.data.get('job', None)
        return self.update(request)


class JobQuestionViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = JobQuestionSerializer
    filter_fields = ('job',)

    def get_queryset(self):
        return JobQuestion.objects.filter(job__pro=self.request.user.pro, job__is_active=True)
