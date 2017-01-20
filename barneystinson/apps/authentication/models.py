from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.core.fields import ImageField


class User(AbstractUser):
    username = models.CharField(_('username'), max_length=250, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    photo = ImageField(_('photo'), blank=True, default='user/photo/default.jpg')
    phone = models.CharField(_('numéro de téléphone'), max_length=250, default='')
    position = models.CharField(_('poste occupé'), max_length=250, default='')
    pro = models.ForeignKey('pro.Pro', blank=True, null=True, verbose_name=_('pro'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email
