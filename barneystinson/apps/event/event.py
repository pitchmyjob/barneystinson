from .models import EventModel


class ApplicantEvent(object):

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

    def __init__(self, id, payload, event):
        self.eventmodel = EventModel(type="ApplicantEvent", id=id, payload=payload)
        self.eventmodel.event = self.EVENTS.get(event)

        if hasattr(self, event):
            getattr(self, event)()

    def save(self):
        self.eventmodel.save()


class JobEvent(object):

    EVENTS = {
        'add_job': 'JobWasAdded',
        'edit_job': 'JobWasModified',
        'delete_job': 'JobWasDeleted'
    }

    def __init__(self, id, payload, event):
        self.eventmodel = EventModel(type="JobEvent", id=id, payload=payload)
        self.eventmodel.event = self.EVENTS.get(event)

        if hasattr(self, event):
            getattr(self, event)()

    def save(self):
        self.eventmodel.save()
