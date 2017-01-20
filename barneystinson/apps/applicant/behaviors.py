from django.db import models
from django.utils.translation import ugettext_lazy as _


class ApplicantRelated(models.Model):
    applicant = models.ForeignKey('applicant.Applicant', verbose_name=_('postulant'))

    class Meta:
        abstract = True


class StartEndDate(models.Model):
    date_start = models.DateField(_('date de début'), null=True, blank=True)
    date_end = models.DateField(_('date de fin'), null=True, blank=True)

    class Meta:
        abstract = True
