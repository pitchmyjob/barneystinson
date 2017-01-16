from .base import *


DEBUG = False

ALLOWED_HOSTS = ['<to_define>']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': get_env_variable('DJANGO_DB_PROD_HOST'),
        'NAME': get_env_variable('DJANGO_DB_PROD_NAME'),
        'USER': get_env_variable('DJANGO_DB_PROD_USER'),
        'PASSWORD': get_env_variable('DJANGO_DB_PROD_PASSWORD'),
    }
}

AWS_STORAGE_BUCKET_NAME = '<to_define>'

EMAIL_BACKEND = '<to_define>'
