from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

from apps.authentication.models import User
from apps.core.api.mixins import IsActiveDestroyMixin

from .permissions import IsProUser
from .serializers import ProSerializer
from ..models import Pro


class ProViewSet(IsActiveDestroyMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 GenericViewSet):
    permission_classes = [permissions.IsAuthenticated, IsProUser]
    serializer_class = ProSerializer

    def get_queryset(self):
        return Pro.objects.filter(pk=self.request.user.pro.pk, is_active=True)

    def perform_destroy(self, instance):
        User.objects.filter(pro=instance).update(is_active=False)
        super(ProViewSet, self).perform_destroy(instance)
