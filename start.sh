#!/bin/bash
gunicorn nombre_proyecto.wsgi:application --bind 0.0.0.0:$PORT
