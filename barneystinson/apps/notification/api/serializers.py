from rest_framework import serializers

from apps.authentication.api.serializers import UserSerializer

from ..models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    emmiter = UserSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ('id', 'type_name', 'emmiter', 'action_object_id', 'created', 'is_unread')
        read_only_fields = ('id', 'type_name', 'emmiter', 'action_object_id', 'created')
