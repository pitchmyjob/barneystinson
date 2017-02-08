from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CandidacyMessage(models.Model):
    candidacy = models.ForeignKey('candidacy.Candidacy', verbose_name=_('candidature'))
    emmiter = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('émmeteur'))
    message = models.TextField(_('message'))
    created = models.DateTimeField(_('date de création'), auto_now_add=True)

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')


class CandidacyMessageRead(models.Model):
    candidacy = models.ForeignKey('candidacy.Candidacy', verbose_name=_('candidature'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('utilisateur'))
    is_read = models.BooleanField(_('est lu'), default=False)
    date = models.DateTimeField(_('date de dernière lecture'), auto_now=True)

    class Meta:
        verbose_name = _('message lu')
        verbose_name_plural = _('messages lu')
        unique_together = ('candidacy', 'user')
