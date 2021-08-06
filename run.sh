#!/bin/bash

# psql -h localhost -p 5432 --username=postgres --password=postgres
# create database uptime;

# npm install -g @vue/cli # install vue
# vue create vue_spa # create vue
# npm run build -- --mode staging

# docker network create traefik_default

export DJANGO_SETTINGS_MODULE=configs.dev

pre-commit run --all-files

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

# uvicorn decoupled_dj.asgi:application
