from django.forms import model_to_dict

from .event import ApplicantEvent, JobEvent


class EventJobMixin(object):
    def transform_object_to_dict(self, object):
        exclude = ('is_active', 'view_counter', 'request_credits')
        job = {}
        for key, value in object.__dict__.items():
            if (isinstance(value, str) or isinstance(value, int) or isinstance(value, list)) and value != "" and value is not None and key not in exclude:
                job[key] = value

        for key, value in object.__dict__['_prefetched_objects_cache'].items():
            job[key] = list(value.values_list("name", flat=True))

        return job

    def perform_update(self, serializer):
        old_object = self.get_object()
        super(EventJobMixin, self).perform_update(serializer)
        new_object = serializer.instance

        if new_object.last_payment:
            if old_object.last_payment:
                event = "edit_job"
            else:
                event = "add_job"

            JobEvent(
                id=new_object.id,
                payload=self.transform_object_to_dict(new_object),
                event=event
            ).save()


class EventApplicantMixin(object):

    def perform_create(self, serializer):
        super(EventApplicantMixin, self).perform_create(serializer)
        
        object = serializer.instance
        run = False

        if self.request.user.is_authenticated():
            if self.request.user.is_applicant:
                run = True
                applicant = self.request.user.applicant if self.event_type != "applicant" else object.applicant
        else:
            if self.event_type == "applicant":
                run = True
                applicant = object.applicant

        if run:
            payload = dict(serializer.validated_data)
            if 'applicant' in payload:
                del payload['applicant']
            if 'photo' in payload:
                del payload['photo']
            payload['id'] = object.id
            ApplicantEvent(
                id=applicant.id,
                payload=payload,
                event="add_" + self.event_type
            ).save()

    def perform_update(self, serializer):
        if self.request.user.is_applicant:
            payload = dict(serializer.validated_data)
            if 'photo' in payload:
                del payload['photo']
            payload['id'] = self.get_object().id
            ApplicantEvent(
                id=self.request.user.applicant.id,
                payload=payload,
                event="edit_" + self.event_type
            ).save()
        super(EventApplicantMixin, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        if self.request.user.is_applicant:
            ApplicantEvent(
                id=self.request.user.applicant.id,
                payload={'id': self.get_object().id},
                event="delete_" + self.event_type
            ).save()
        super(EventApplicantMixin, self).perform_destroy(serializer)
