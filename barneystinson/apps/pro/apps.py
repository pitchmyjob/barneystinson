from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProConfig(AppConfig):
    name = 'apps.pro'
    verbose_name = _('Pros')
