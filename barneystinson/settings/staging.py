from .production import *  # noqa


INSTALLED_APPS += [
    # Thirds apps
    'corsheaders',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': get_env_variable('DJANGO_DB_STAGING_HOST'),
        'NAME': get_env_variable('DJANGO_DB_STAGING_NAME'),
        'USER': get_env_variable('DJANGO_DB_STAGING_USER'),
        'PASSWORD': get_env_variable('DJANGO_DB_STAGING_PASSWORD'),
    }
}

MIDDLEWARE = MIDDLEWARE + ['corsheaders.middleware.CorsMiddleware']

RAVEN_CONFIG = {
    'dsn': 'https://05865ad797e943bf8d98bcd2159e8c2b:e602a262b83e47f7aa4528c03e252c96@sentry.io/134978',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}

# AWS_STORAGE_BUCKET_NAME = '<to_define>'

REST_FRAMEWORK_DOCS = {
    'HIDE_DOCS': False
}

EVENT_LOG = "EventLog-staging"

SNS_EMAIL = "arn:aws:sns:eu-west-1:074761588836:sendEmail-staging"
SQS_EMAIL = "v2-sqsEmail-staging"

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken'
)
