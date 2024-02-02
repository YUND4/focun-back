#!/bin/bash

while ! timeout 1 bash -c "echo > /dev/tcp/$POSTGRES_HOST/$POSTGRES_PORT"; do
  echo "PostgreSQL is not ready, retrying..."
  sleep 1
done


if [ "$RUNTIME_MODE" = "test" ]; then
    clear
    pytest --reuse-db
    exit 0
fi

if [ "$RUNTIME_MODE" = "dev" ]; then
  if [ "$SERVICE_TYPE" = "web" ]; then
    python manage.py runserver 0.0.0.0:8000
  elif [ "$SERVICE_TYPE" = "celery" ]; then
    celery -A back worker --loglevel=debug
  fi
else
  if [ "$SERVICE_TYPE" = "web" ]; then
    python manage.py migrate
    gunicorn back.wsgi:application --bind 0.0.0.0:8000
  elif [ "$SERVICE_TYPE" = "celery" ]; then
    celery -A back worker --loglevel=info
  fi
fi
