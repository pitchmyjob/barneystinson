from django.contrib.contenttypes.models import ContentType
from django.db.models.query import QuerySet

from .models import Notification


class NotificationHandler(object):
    def __init__(self, type_name, emmiter, action_object):
        self.type_name = type_name
        self.emmiter = emmiter
        self.action_object = action_object

    def send(self):
        method_name = 'perform_{}'.format(self.type_name).lower()
        method = getattr(self, method_name, None)
        if method:
            method()

    def send_notification(self, receivers):
        if isinstance(receivers, QuerySet):
            receivers = list(receivers.all())
        elif not isinstance(receivers, list):
            receivers = [receivers]

        action_object_content_type = ContentType.objects.get_for_model(self.action_object.__class__)

        instances = []
        for receiver in receivers:
            instances.append(Notification(type_name=self.type_name, emmiter=self.emmiter, receiver=receiver,
                                          action_object_content_type=action_object_content_type,
                                          action_object_id=self.action_object.pk))
        return Notification.objects.bulk_create(instances)

    def send_email(self, template, subject, context, receivers):
        pass

    def perform_applicant_job_new_matching(self):
        pass

    def perform_applicant_candidacy_requested(self):
        self.send_notification(self.action_object.applicant.user)

    def perform_applicant_candidacy_approved(self):
        pass

    def perform_applicant_candidacy_disapproved(self):
        pass

    def perform_applicant_candidacy_new_message(self):
        pass

    def perform_pro_job_added(self):
        pass

    def perform_pro_job_updated(self):
        pass

    def perform_pro_job_published(self):
        pass

    def perform_pro_job_deleted(self):
        pass

    def perform_pro_job_liked(self):
        self.send_notification(self.action_object.job.pro.user_set.filter(is_active=True))

    def perform_pro_job_new_candidacy(self):
        self.send_notification(self.action_object.job.pro.user_set.filter(is_active=True))

    def perform_pro_collaborator_added(self):
        pass

    def perform_pro_collaborator_deleted(self):
        pass

    def perform_pro_candidacy_new_message(self):
        pass

    def perform_pro_candidacy_new_comment(self):
        pass
