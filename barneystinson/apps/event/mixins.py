import inspect

from rest_framework.renderers import JSONRenderer

from .event import ApplicantEvent

class EventApplicantMixin(object):

    def perform_create(self, serializer):
        payload = dict(serializer.validated_data)
        if 'applicant' in payload:
            del payload['applicant']
        object = serializer.save()
        payload['id'] = object.id
        ApplicantEvent(id=self.request.user.applicant.id, payload=payload, event="add_" + self.event_type).save()

    def perform_update(self, serializer):
        payload = serializer.validated_data
        payload['id'] = self.get_object().id
        ApplicantEvent(id=self.request.user.applicant.id, payload=payload, event="edit_"+self.event_type).save()
        super(EventApplicantMixin, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        ApplicantEvent(id=self.request.user.applicant.id, payload={'id' : self.get_object().id}, event="delete_"+self.event_type).save()
        super(EventApplicantMixin, self).perform_destroy(serializer)
