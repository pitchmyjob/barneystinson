from rest_framework import mixins
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import GenericViewSet

from apps.authentication.models import User
from apps.core.api.mixins import IsAuthenticatedMixin, IsActiveDestroyMixin

from ..models import Pro
from .serializers import ProSerializer, ProRegisterSerializer


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


class ProRegisterAPIView(CreateAPIView):
    serializer_class = ProRegisterSerializer

    def perform_create(self, serializer):
        data = serializer.data
        pro = Pro.objects.create(**data['pro'])
        user = User.objects.create_user(username=data['user']['email'], pro=pro, **data['user'])
        del serializer.data['user']['password']
        serializer.data['user']['token'] = user.auth_token.key
