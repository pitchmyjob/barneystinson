from django.conf import settings

from storages.backends.s3boto import S3BotoStorage


StaticStorage = lambda: S3BotoStorage(location=settings.STATICFILES_LOCATION)  # noqa
MediaStorage = lambda: S3BotoStorage(location=settings.MEDIAFILES_LOCATION)  # noqa
