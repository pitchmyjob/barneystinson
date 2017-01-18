from model_utils.models import TimeStampedModel

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.core.behaviors import Localisation


class Job(Localisation, TimeStampedModel, models.Model):
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

    class Meta:
        verbose_name = _('offre')
        verbose_name_plural = _('offres')

    def __str__(self):
        return self.title


class JobQuestion(models.Model):
    job = models.ForeignKey('job.Job', related_name='questions', null=True, blank=True)
    question = models.CharField(max_length=250)
    order = models.PositiveSmallIntegerField(_('ordre'), default=1)

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')
        ordering = ['order']

    def __str__(self):
        return self.question
