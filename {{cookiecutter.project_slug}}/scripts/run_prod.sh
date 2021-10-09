#!/bin/bash

set -e

bash /app/scripts/prestart.sh

echo "Run Collectstatic"
python /app/manage.py collectstatic --noinput --clear --settings=${DJANGO_SETTINGS_MODULE?Variable Not Set}

gunicorn {{cookiecutter.project_slug}}.wsgi:application --bind 0.0.0.0:8000