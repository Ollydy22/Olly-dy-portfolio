#!/bin/bash



# Exit on error
set -e

echo "Building project..."
python3.9 -m pip install -r requirements.txt

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear
