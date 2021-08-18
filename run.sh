#!/bin/bash

# clear all admin default table
# python manage.py migrate admin zero
# python manage.py migrate auth zero
# python manage.py migrate contenttypes zero
# python manage.py migrate sessions zero

# psql -h localhost -p 5432 --username=postgres --password=postgres
# create database uptime;

# npm install -g @vue/cli # install vue
# vue create vue_spa # create vue
# npm run build -- --mode staging

# docker network create traefik_default

export DJANGO_SETTINGS_MODULE=configs.dev

# pre-commit run --all-files

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

# uvicorn decoupled_dj.asgi:application

# ./manage.py test --pattern="tests_*.py"
