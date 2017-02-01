from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.core.api.mixins import IsAuthenticatedMixin

from ..models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(IsAuthenticatedMixin, ListModelMixin, GenericViewSet):
    serializer_class = NotificationSerializer
    filter_fields = ('is_unread',)

    def get_queryset(self):
        return Notification.objects.filter(receiver=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super(NotificationViewSet, self).list(request, args, **kwargs)
        Notification.objects.filter(receiver=request.user, is_unread=True).update(is_unread=False)
        return response
