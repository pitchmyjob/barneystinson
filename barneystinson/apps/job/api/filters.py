import datetime

import django_filters

from django.conf import settings
from django.utils import timezone

from ..models import Job


class JobFilter(django_filters.rest_framework.FilterSet):
    is_pending = django_filters.CharFilter(method='get_is_pending')
    is_visible = django_filters.CharFilter(method='get_is_visible')
    is_expired = django_filters.CharFilter(method='get_is_expired')

    class Meta:
        model = Job
        fields = ('is_pending', 'is_visible', 'is_expired')

    def get_is_pending(self, queryset, name, value):
        return queryset.filter(last_payment__isnull=True)

    def get_is_visible(self, queryset, name, value):
        date = timezone.now() - datetime.timedelta(days=settings.DAYS_JOB)
        return queryset.filter(last_payment__gte=date)

    def get_is_expired(self, queryset, name, value):
        date = timezone.now() - datetime.timedelta(days=settings.DAYS_JOB)
        return queryset.filter(last_payment__lt=date)
