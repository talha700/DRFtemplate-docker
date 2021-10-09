#!/bin/bash

set -e

bash /app/scripts/prestart.sh
echo $DJANGO_SETTINGS_MODULE
python /app/manage.py runserver 0.0.0.0:80 --settings=${DJANGO_SETTINGS_MODULE?Variable Not Set}