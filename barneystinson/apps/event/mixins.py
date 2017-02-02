from .event import ApplicantEvent, JobEvent
from apps.job.api.serializers import JobEventSerializer


class EventJobMixin(object):
    def remove_empty_and_ordereddict(self, datas):
        job = {k: v for k, v in datas.items() if v}
        job['experiences'] = [dict(v) for v in datas['experiences']]
        job['contract_types'] = [dict(v) for v in datas['contract_types']]
        job['study_levels'] = [dict(v) for v in datas['study_levels']]
        job['pro'] = dict({k: v for k, v in datas['pro'].items() if v})

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

            datas = JobEventSerializer(instance=serializer.instance).data

            JobEvent(
                id=new_object.id,
                payload=self.remove_empty_and_ordereddict(datas),
                event=event
            ).save()

    def perform_destroy(self, serializer):
        JobEvent(
            id=self.get_object().id,
            payload={},
            event="delete_job"
        ).save()
        super(EventJobMixin, self).perform_destroy(serializer)


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
            if "photo" in payload:
                payload['photo'] = str(serializer.instance.photo)
            payload['id'] = object.id
            ApplicantEvent(
                id=applicant.id,
                payload=payload,
                event="add_" + self.event_type
            ).save()

    def perform_update(self, serializer):
        super(EventApplicantMixin, self).perform_update(serializer)

        if self.request.user.is_applicant:
            payload = dict(serializer.validated_data)
            if "photo" in payload:
                payload['photo'] = str(serializer.instance.photo)
            payload['id'] = self.get_object().id
            ApplicantEvent(
                id=self.request.user.applicant.id,
                payload=payload,
                event="edit_" + self.event_type
            ).save()

    def perform_destroy(self, serializer):
        if self.request.user.is_applicant:
            ApplicantEvent(
                id=self.request.user.applicant.id,
                payload={'id': self.get_object().id},
                event="delete_" + self.event_type
            ).save()
        super(EventApplicantMixin, self).perform_destroy(serializer)
