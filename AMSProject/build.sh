#!/usr/bin/env bash
# exit on error
set -o errexit

#pip install -r requirements.txt
pip install --upgrade pip

pip install pipenv

pipenv shell

pipenv install

#python manage.py collectstatic --no-input
python manage.py migrate