from .base import *  # noqa


DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = []

INSTALLED_APPS += [
    # Thirds apps
    'django_extensions',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': get_env_variable('DJANGO_DB_DEV_HOST'),
        'NAME': get_env_variable('DJANGO_DB_DEV_NAME'),
        'USER': get_env_variable('DJANGO_DB_DEV_USER'),
        'PASSWORD': get_env_variable('DJANGO_DB_DEV_PASSWORD'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EVENT_LOG = "dev-EventLog"
