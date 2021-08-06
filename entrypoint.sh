#!/bin/bash

# set env
export PROJECT_ID=livestreaming-241004
export LOCATION_ID=us-central1

python3 manage.py runserver 0.0.0.0:8080
# uvicorn decoupled_dj.asgi:application