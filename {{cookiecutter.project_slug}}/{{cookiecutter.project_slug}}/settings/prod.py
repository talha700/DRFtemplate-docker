"""
Settings file for staging production server
"""
from datetime import timedelta

from .base import *  # noqa: 403
from os import getenv

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': getenv('POSTGRES_USER'),
        'PASSWORD': getenv('POSTGRES_PASSWORD'),
        'NAME': getenv('POSTGRES_DB'),
        'HOST': getenv('POSTGRES_SERVER'),
        'PORT': getenv('POSTGRES_PORT')
    },
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': getenv('SECRET_KEY'),
}
