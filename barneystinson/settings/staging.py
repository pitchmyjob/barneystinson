from .production import *  # noqa


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': get_env_variable('DJANGO_DB_STAGING_HOST'),
        'NAME': get_env_variable('DJANGO_DB_STAGING_NAME'),
        'USER': get_env_variable('DJANGO_DB_STAGING_USER'),
        'PASSWORD': get_env_variable('DJANGO_DB_STAGING_PASSWORD'),
    }
}

# AWS_STORAGE_BUCKET_NAME = '<to_define>'

REST_FRAMEWORK_DOCS = {
    'HIDE_DOCS': False
}

EVENT_LOG = "EventLog-staging"

SNS_EMAIL = "arn:aws:sns:eu-west-1:074761588836:sendEmail-staging"
SQS_EMAIL = "v2-sqsCronEmail-staging"