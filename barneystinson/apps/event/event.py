from .models import EventModel


class EventMixin(object):
    TYPE = None
    EVENTS = None

    def __init__(self, id, payload, event):
        self.eventmodel = EventModel(type=self.TYPE, id=id, payload=payload)
        self.eventmodel.event = self.EVENTS.get(event)

        if hasattr(self, event):
            getattr(self, event)()

    def save(self):
        self.eventmodel.save()


class ApplicantEvent(EventMixin):
    TYPE = 'ApplicantEvent'
    EVENTS = {
        'add_applicant': 'ApplicantWasAdded',
        'edit_applicant': 'ApplicantWasModified',
        'add_experience': 'ExperienceWasAdded',
        'edit_experience': 'ExperienceWasModified',
        'delete_experience': 'ExperienceWasDeleted',
        'add_education': 'EducationWasAdded',
        'edit_education': 'EducationWasModified',
        'delete_education': 'EducationWasDeleted',
        'add_skill': 'SkillWasAdded',
        'edit_skill': 'SkillWasModified',
        'delete_skill': 'SkillWasDeleted',
        'add_interest': 'InterestWasAdded',
        'edit_interest': 'InterestWasModified',
        'delete_interest': 'InterestWasDeleted',
        'add_language': 'LanguageWasAdded',
        'edit_language': 'LanguageWasModified',
        'delete_language': 'LanguageWasDeleted',
    }


class JobEvent(EventMixin):
    TYPE = 'JobEvent'
    EVENTS = {
        'add_job': 'JobWasAdded',
        'edit_job': 'JobWasModified',
        'delete_job': 'JobWasDeleted'
    }
