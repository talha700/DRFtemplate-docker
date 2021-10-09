"""
WSGI config for {{cookiecutter.project_slug}} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if not os.getenv('DJANGO_SETTINGS_MODULE'):
    raise EnvironmentError('DJANGO_SETTINGS_MODULE environmental variable is not set!')

application = get_wsgi_application()
