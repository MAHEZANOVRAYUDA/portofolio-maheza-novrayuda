#!/usr/bin/env bash
set -e

echo "==> Install Python dependencies"
pip install -r requirements.txt

echo "==> Install & build frontend assets"
npm install
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --minify

echo "==> Django system check"
python3 manage.py check --deploy

echo "==> Collect static files"
python3 manage.py collectstatic --noinput
