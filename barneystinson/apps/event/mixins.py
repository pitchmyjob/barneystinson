from .event import ApplicantEvent


class EventApplicantMixin(object):

    def perform_create(self, serializer):
        object = serializer.save()
        if hasattr(self.request.user, 'applicant'):
            payload = dict(serializer.validated_data)
            if 'applicant' in payload:
                del payload['applicant']
            payload['id'] = object.id
            ApplicantEvent(
                id=self.request.user.applicant.id,
                payload=payload,
                event="add_" + self.event_type
            ).save()

    def perform_update(self, serializer):
        if hasattr(self.request.user, 'applicant'):
            payload = serializer.validated_data
            payload['id'] = self.get_object().id
            ApplicantEvent(
                id=self.request.user.applicant.id,
                payload=payload,
                event="edit_" + self.event_type
            ).save()
        super(EventApplicantMixin, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        if hasattr(self.request.user, 'applicant'):
            ApplicantEvent(
                id=self.request.user.applicant.id,
                payload={'id': self.get_object().id},
                event="delete_" + self.event_type
            ).save()
        super(EventApplicantMixin, self).perform_destroy(serializer)
