from django.core.exceptions import ImproperlyConfigured

from .utils import NotificationHandler


class NotificationtMixin(object):
    notification_type = None
    map_url_to_notification_type = None

    def send_notification(self, instance, emitter):
        if not self.notification_type and not self.map_url_to_notification_type:
            raise ImproperlyConfigured('"%s" should include a `notification_type` or `map_url_to_notification_type`'
                                       'attribute.' % self.__class__.__name__)
        if self.notification_type:
            notification_type = self.notification_type
        else:
            notification_type = self.map_url_to_notification_type.get(self.request.resolver_match.url_name)
        NotificationHandler(type_name=self.notification_type, emmiter=emitter, action_object=instance).send()

    def perform_create(self, serializer):
        super(NotificationtMixin, self).perform_create(serializer)
        self.send_notification(serializer.instance, self.request.user)

    def perform_update(self, serializer):
        super(NotificationtMixin, self).perform_update(serializer)
        self.send_notification(serializer.instance, self.request.user)

    def perform_destroy(self, serializer):
        super(NotificationtMixin, self).perform_destroy(serializer)
        self.send_notification(serializer.instance, self.request.user)
