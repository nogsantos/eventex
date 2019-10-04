#!/bin/bash

echo 'Generation static files'

python manage.py collectstatic --noinput
