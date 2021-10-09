"""
Settings file for development. Davit Mikava
"""
from datetime import timedelta
from os import getenv
from .base import *  # noqa: 403


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': getenv('POSTGRES_USER', 'dev'),
        'PASSWORD': getenv('POSTGRES_PASSWORD', 'dev'),
        'NAME': getenv('POSTGRES_DB', 'internal_software'),
        'HOST': getenv('POSTGRES_SERVER', '127.0.0.1'),
        'PORT': getenv('POSTGRES_PORT', 5432)
    },
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=600),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': getenv('SECRET_KEY'),
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
