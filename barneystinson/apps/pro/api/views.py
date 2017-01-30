from rest_framework import generics, permissions

from apps.authentication.models import User
from apps.core.api.mixins import IsActiveDestroyMixin

from .permissions import IsProUser
from .serializers import ProSerializer
from ..models import Pro


class ProMeAPIView(IsActiveDestroyMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions, IsProUser]
    serializer_class = ProSerializer
    queryset = Pro.objects.none()

    def perform_destroy(self, instance):
        User.objects.filter(pro=instance).update(is_active=False)
        super(ProMeAPIView, self).perform_destroy(instance)

    def get_object(self):
        return self.request.user.pro
