#!/bin/bash

set -e

echo "Waiting for database connection..."
while ! nc -z ${DATABASE_HOST} ${DATABASE_PORT}; do
  sleep 1
done
echo "Database is available!"

echo "Applying database migrations..."
alembic upgrade head

echo "Starting FastAPI application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000