from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.core.behaviors import Localisation
from apps.core.utils import generate_upload_to


class Pro(Localisation, models.Model):
    company = models.CharField(_('raison sociale'), max_length=250)
    website = models.CharField(_('site web'), max_length=250, blank=True)
    description = models.TextField(_('description'), max_length=250, blank=True)
    phone = models.CharField(_('phone'), max_length=250, blank=True)
    industry = models.ForeignKey('data.Industry', default=1, verbose_name=_('secteur d\'activité'))
    employes = models.ForeignKey('data.Employee', null=True, verbose_name=_('nombre d\'employés'))
    ca = models.CharField(_('chiffre d\'affaire'), max_length=250, blank=True)
    video_url = models.CharField(_('vidéo'), max_length=250, blank=True)
    image = models.ImageField(_('logo'), upload_to=generate_upload_to, default='pro/default.jpg')

    def __str__(self):
        return self.company
