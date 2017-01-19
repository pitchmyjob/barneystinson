from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AuthenticationConfig(AppConfig):
    name = 'apps.authentication'
    verbose_name = _('Utilisateurs')

    def ready(self):
        import apps.authentication.signals  # noqa
