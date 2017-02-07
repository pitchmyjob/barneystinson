import datetime

from django.forms.models import model_to_dict

from .event import ApplicantEvent, JobEvent


class CoreEventJob(object):
    job_id = None
    topush = {}

    def dict_to_push(self, validated_data):
        self.topush = {}
        for key, data in validated_data.items():
            if data is None or data == "":
                continue
            elif key == "experiences":
                self.topush[key] = [model_to_dict(v) for v in data]
            elif key == "contract_types":
                self.topush[key] = [model_to_dict(v) for v in data]
            elif key == "study_levels":
                self.topush[key] = [model_to_dict(v) for v in data]
            else:
                self.topush[key] = data

    def initial_dict_to_push(self, instance):
        self.topush = {
            "title": instance.title,
            "description": instance.description,
            "skills": instance.skills,
            "salary": instance.salary,
            "contract_types": [model_to_dict(k) for k in instance.contract_types.all()],
            "experiences": [model_to_dict(k) for k in instance.experiences.all()],
            "study_levels": [model_to_dict(k) for k in instance.study_levels.all()],
            "last_payment": str(instance.last_payment),
            "pro": {
                "id": instance.pro.id,
                "logo": str(instance.pro.logo),
                "company": instance.pro.company
            }
        }

    def push_event(self, action):
        JobEvent(
            id=self.job_id,
            payload=self.topush,
            event=action
        ).save()


class CoreEventApplicant(object):

    topush = {}
    applicant_id = None

    def push_event(self, action):
        ApplicantEvent(
            id=self.applicant_id if self.applicant_id else self.request.user.applicant.id,
            payload=self.topush,
            event=action + "_" + self.event_type
        ).save()

    def create_dict_to_push(self, datas):
        self.topush = {}
        for key, data in datas.items():
            if key == "applicant" or data is None or data == "" or key == "password":
                continue
            if isinstance(data, list):
                self.topush[key] = data
            if key == "photo":
                self.topush[key] = str(self.request.user.photo) if self.request.user.is_authenticated() else str(data)
            if key == "wanted_contracts":
                self.topush[key] = [str(v.name) for v in data]
            if isinstance(data, str):
                self.topush[key] = str(data)
            if isinstance(data, datetime.date) and data:
                self.topush[key] = str(data)
