#!/bin/bash

set -e

DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME-admin}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD-adminamdin}
DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL-admin@admin.com}

while ! nc -z $POSTGRES_SERVER $POSTGRES_PORT; do
  sleep 0.1
done

# Run makemigration, migration
echo "Run makemigrations"
python /app/manage.py makemigrations --settings=${DJANGO_SETTINGS_MODULE?Variable Not Set}
echo "Run migrate"
python /app/manage.py migrate --settings=${DJANGO_SETTINGS_MODULE?Variable Not Set}
echo "Create superuser"
python /app/manage.py createsuperuser --noinput --settings=${DJANGO_SETTINGS_MODULE?Variable Not Set}  || true
