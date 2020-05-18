#!/bin/bash

echo "Waiting for postgres..."

# Wait for the postgres server to spin up
python scripts/wait.py

echo "PostgreSQL started"

# Update and upgrade the database
flask db migrate -m "setup"
flask db upgrade

# Run the web server
gunicorn wsgi --bind 0.0.0.0:8000
