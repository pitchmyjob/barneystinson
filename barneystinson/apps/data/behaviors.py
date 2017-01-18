from django.db import models
from django.utils.translation import ugettext_lazy as _


class DataModel(models.Model):
    name = models.CharField(_('nom'), max_length=250)
    is_active = models.BooleanField(_('est actif'), default=True)
    order = models.PositiveSmallIntegerField(_('ordre'), default=1)

    class Meta:
        abstract = True
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
