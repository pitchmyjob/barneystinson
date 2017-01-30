from rest_framework import generics, mixins, permissions
from rest_framework.viewsets import GenericViewSet

from apps.authentication.models import User
from apps.core.api.mixins import IsActiveDestroyMixin

from .permissions import IsProUser
from .serializers import ProSerializer, UserRegisterCollaboratorSerializer
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


class ProCollaboratorViewSet(IsActiveDestroyMixin,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             GenericViewSet):
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions, IsProUser]
    serializer_class = UserRegisterCollaboratorSerializer
    queryset = User.objects.none()

    def get_queryset(self):
        return User.objects.filter(pro=self.request.user.pro, is_active=True)
