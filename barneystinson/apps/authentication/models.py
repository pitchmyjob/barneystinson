from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.core.utils import generate_upload_to


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    image = models.ImageField(_('photo'), upload_to=generate_upload_to, blank=True)
    pro = models.ForeignKey('pro.Pro', blank=True, null=True, verbose_name=_('pro'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email
