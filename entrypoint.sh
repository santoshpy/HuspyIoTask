#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
echo "Database Migrate..."
python manage.py migrate --no-input
echo "Running TestCase..."
python manage.py tests --no-input

exec "$@"