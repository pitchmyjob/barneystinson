from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from django.utils import timezone

from apps.notification import types
from apps.notification.api.mixins import NotificationtMixin
from apps.pro.api.permissions import IsProUser

from ..models import CandidacyMessage, CandidacyMessageRead
from .serializers import CandidacyMessageSerializer, CandidacyMessageJobListSerializer


class CandidacyMessageViewSet(NotificationtMixin, ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CandidacyMessageSerializer
    filter_fields = ('candidacy',)

    def get_notification_type(self):
        if self.action == 'create':
            if self.request.user.is_pro:
                return types.PRO_CANDIDACY_NEW_MESSAGE
            elif self.request.user.is_applicant:
                return types.APPLICANT_CANDIDACY_NEW_MESSAGE

    def get_queryset(self):
        qs_filter = {}
        if self.request.user.is_pro:
            qs_filter = {'candidacy__job__pro': self.request.user.pro}
        elif self.request.user.is_applicant:
            qs_filter = {'candidacy__applicant': self.request.user.applicant}
        return CandidacyMessage.objects.filter(**qs_filter)

    def list(self, request, *args, **kwargs):
        response = super(CandidacyMessageViewSet, self).list(request, *args, **kwargs)
        candidacy_id = self.request.GET.get('candidacy')
        if candidacy_id:
            qs_filter = {'user': self.request.user, 'candidacy_id': candidacy_id}
            candidacy_messsage_read, created = CandidacyMessageRead.objects.get_or_create(**qs_filter)
            candidacy_messsage_read.is_read = True
            candidacy_messsage_read.date = timezone.now()
            candidacy_messsage_read.save()
        return response


class CandidacyMessageJobListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = CandidacyMessageJobListSerializer

    def get_queryset(self):
        qs_filter = {
            'candidacy__job': self.kwargs.get('pk'),
            'candidacy__job__pro': self.request.user.pro,
        }
        queryset = CandidacyMessage.objects.filter(**qs_filter).select_related('candidacy__applicant__user', 'emmiter')
        return queryset.distinct('candidacy__id').order_by('candidacy__id', '-created')

    def get_serializer_context(self):
        context = super(CandidacyMessageJobListAPIView, self).get_serializer_context()
        qs_filter = {
            'candidacy__job': self.kwargs.get('pk'),
            'candidacy__job__pro': self.request.user.pro,
        }
        reads = CandidacyMessageRead.objects.filter(**qs_filter)
        context['is_reads'] = {obj.candidacy_id: (obj.is_read, obj.date) for obj in reads}
        return context
