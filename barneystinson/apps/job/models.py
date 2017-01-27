import datetime

from model_utils.models import TimeStampedModel

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from apps.core.behaviors import Localisation

from .managers import JobManager


class Job(Localisation, TimeStampedModel, models.Model):
    STATE_PENDING_LABEL = _('En attente')
    STATE_VISIBLE_LABEL = _('Visible')
    STATE_EXPIRED_LABEL = _('Expirée')

    pro = models.ForeignKey('pro.Pro', blank=True, null=True, verbose_name=_('pro'))
    title = models.CharField(_('titre de l\'offre'), max_length=250)
    contract_types = models.ManyToManyField('data.ContractType', verbose_name=_('types de contrat'))
    experiences = models.ManyToManyField('data.Experience', verbose_name=_('expériences'))
    study_levels = models.ManyToManyField('data.StudyLevel', verbose_name=_('niveaux d\'étude'))
    salary = models.CharField(_('salaire'), max_length=250)
    skills = ArrayField(models.CharField(_('skill'), max_length=250), verbose_name=_('compétences recherchées'))
    description = models.TextField(_('description'))
    view_counter = models.PositiveIntegerField(_('nombre de vue'), default=0)
    last_payment = models.DateTimeField(_('dernier paiement'), null=True, blank=True)
    is_active = models.BooleanField(_('est actif'), default=True)
    request_credits = models.PositiveIntegerField(_('crédits demande d\'entretien'), default=0)

    objects = JobManager

    class Meta:
        verbose_name = _('offre')
        verbose_name_plural = _('offres')

    def __str__(self):
        return self.title

    def get_state(self):
        date = timezone.now() - datetime.timedelta(days=settings.DAYS_JOB)
        if self.last_payment is None:
            return self.STATE_PENDING_LABEL
        elif self.last_payment >= date:
            return self.STATE_VISIBLE_LABEL
        else:
            return self.STATE_EXPIRED_LABEL
    get_state.short_description = _('État')


class JobQuestion(models.Model):
    job = models.ForeignKey('job.Job', related_name='questions', verbose_name=_('offre'))
    question = models.CharField(_('question'), max_length=250)
    order = models.PositiveSmallIntegerField(_('ordre'), default=1)

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')
        ordering = ['order']

    def __str__(self):
        return self.question
