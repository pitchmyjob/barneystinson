from rest_framework import decorators, permissions
from rest_framework.viewsets import ModelViewSet

from apps.core.api.mixins import IsActiveDestroyMixin
from apps.notification import types
from apps.notification.api.mixins import NotificationtMixin
from apps.pro.api.permissions import IsProUser
from apps.event.mixins import EventJobMixin

from ..models import Job, JobQuestion
from .filters import JobFilter
from .serializers import JobSerializer, JobQuestionSerializer, JobPublishSerializer


class JobViewSet(NotificationtMixin, IsActiveDestroyMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = JobSerializer
    map_action_to_notification_type = {
        'create': types.PRO_JOB_ADDED,
        'update': types.PRO_JOB_UPDATED,
        'destroy': types.PRO_JOB_DELETED,
    }
    filter_class = JobFilter
    search_fields = ('title', 'description')

    def get_queryset(self):
        qs = Job.objects.prefetch_related('contract_types', 'experiences', 'study_levels')
        return qs.filter(pro=self.request.user.pro, is_active=True)

    @decorators.list_route(methods=['put', 'patch'], serializer_class=JobPublishSerializer,
                           notification_type=types.PRO_JOB_PUBLISHED)
    def publish(self, request, pk=None):
        self.kwargs['pk'] = request.data.get('job', None)
        return self.update(request)


class JobQuestionViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = JobQuestionSerializer
    filter_fields = ('job',)

    def get_queryset(self):
        return JobQuestion.objects.filter(job__pro=self.request.user.pro, job__is_active=True)
