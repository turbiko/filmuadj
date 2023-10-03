#!/bin/sh

#if [ "$DATABASE" = "postgres" ]
#then
#    echo "Waiting for postgres..."
#    echo "HOST: "$SQL_HOST $SQL_PORT
#
#    while ! nc -z $SQL_HOST $SQL_PORT; do
#      sleep 0.1
#    done
#
#    echo "PostgreSQL started"
#fi
echo "production started...."
#python manage.py makemigrations --settings=core.settings.production
python manage.py migrate --settings=zakupivli.settings.production
python manage.py collectstatic --settings=zakupivli.settings.production --no-input --clear
python manage.py update_index --settings=zakupivli.settings.production
gunicorn zakupivli.wsgi:application -b :8000  --workers=5   --timeout=190 --graceful-timeout=100 --log-level=DEBUG --reload
exec "$@"