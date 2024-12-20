#!/bin/sh

echo "gunicorn -w 1 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --access-logfile - main:app"
gunicorn -w 1 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --access-logfile - main:app
