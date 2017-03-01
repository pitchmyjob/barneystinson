from rest_framework import decorators, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from django.db.models import Count

from apps.candidacy.models import Candidacy
from apps.core.api.mixins import IsActiveDestroyMixin
from apps.notification import types
from apps.notification.api.mixins import NotificationtMixin
from apps.pro.api.permissions import IsProUser
from apps.event.mixins import EventJobViewSetMixin

from ..models import Job, JobQuestion
from .filters import JobFilter
from .pagination import JobPagination
from .serializers import JobSerializer, JobQuestionSerializer, JobPublishSerializer


class JobViewSet(EventJobViewSetMixin, NotificationtMixin, IsActiveDestroyMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = JobSerializer
    pagination_class = JobPagination
    map_action_to_notification_type = {
        'create': types.PRO_JOB_ADDED,
        'update': types.PRO_JOB_UPDATED,
        'destroy': types.PRO_JOB_DELETED,
    }
    filter_class = JobFilter
    search_fields = ('title', 'description')

    def get_serializer_context(self):
        context = super(JobViewSet, self).get_serializer_context()

        not_matching = Candidacy.objects.filter(job__pro=self.request.user.pro).exclude(status=Candidacy.MATCHING)
        candidacies_count = Job.objects.filter(candidacy__in=not_matching).annotate(Count('candidacy')) \
                                       .values('id', 'candidacy__count')
        context['candidacies_count'] = {job['id']: job['candidacy__count'] for job in candidacies_count}
        return context

    def get_queryset(self):
        qs = Job.objects.prefetch_related('contract_types', 'experiences', 'study_levels')
        return qs.filter(pro=self.request.user.pro, is_active=True)

    @decorators.list_route(methods=['put', 'patch'], serializer_class=JobPublishSerializer,
                           notification_type=types.PRO_JOB_PUBLISHED)
    def publish(self, request, pk=None):
        self.kwargs['pk'] = request.data.get('job', None)
        return self.update(request)

    @decorators.list_route(methods=['get'])
    def count(self, request, pk=None):
        return Response({
            'pending': Job.objects.filter(pro=request.user.pro, is_active=True).is_pending().count(),
            'visible': Job.objects.filter(pro=request.user.pro, is_active=True).is_visible().count(),
            'expired': Job.objects.filter(pro=request.user.pro, is_active=True).is_expired().count(),
        })


class JobQuestionViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = JobQuestionSerializer
    filter_fields = ('job',)

    def get_queryset(self):
        return JobQuestion.objects.filter(job__pro=self.request.user.pro, job__is_active=True)
