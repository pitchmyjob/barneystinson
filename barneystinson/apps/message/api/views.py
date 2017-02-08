from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from django.utils import timezone

from apps.notification import types
from apps.notification.api.mixins import NotificationtMixin

from ..models import CandidacyMessage, CandidacyMessageRead
from .serializers import CandidacyMessageSerializer


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
            CandidacyMessageRead.objects.filter(**qs_filter).update(is_read=True, date=timezone.now())
        return response
