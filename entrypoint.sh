#!/bin/bash

echo "Waiting for MySQL..."

# Wait for MySQL to be available on the db:3306 port
dockerize -wait tcp://db:3306 -timeout 30s

echo "MySQL started"

echo "Running migrate..."
flask db migrate
flask db upgrade
flask load-data

echo "Starting server..."
# Start the application using Gunicorn
exec gunicorn --bind 0.0.0.0:5000 --workers 2 app:app