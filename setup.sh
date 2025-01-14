#!/bin/bash

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate

# Create superuser if needed (you'll do this manually through Heroku CLI) 