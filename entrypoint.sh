#!/bin/bash

while ! timeout 1 bash -c "echo > /dev/tcp/$POSTGRES_HOST/$POSTGRES_PORT"; do
  echo "PostgreSQL is not ready, retrying..."
  sleep 1
done

python manage.py migrate

if [ "$RUNTIME_MODE" = "dev" ]; then
  python manage.py runserver 0.0.0.0:8000
else
  gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
fi
