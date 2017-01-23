from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.authentication.models import User
from apps.core.api.mixins import IsAuthenticatedMixin, IsActiveDestroyMixin

from ..models import Pro
from .serializers import ProSerializer


class ProViewSet(IsAuthenticatedMixin,
                 IsActiveDestroyMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 GenericViewSet):
    serializer_class = ProSerializer

    def get_queryset(self):
        pro = self.request.user.pro
        if pro:
            return Pro.objects.filter(pk=pro.pk, is_active=True)
        return Pro.objects.none()

    def perform_destroy(self, instance):
        User.objects.filter(pro=instance).update(is_active=False)
        super(ProViewSet, self).perform_destroy(instance)
