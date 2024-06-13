#!/bin/bash
source venv/bin/activate
exec gunicorn --bind 0.0.0.0:8000 app:app
