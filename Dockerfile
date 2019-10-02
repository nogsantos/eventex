FROM python:3.7

RUN mkdir /eventex
WORKDIR /eventex
COPY ./requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev &&  \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/archive/*.deb

RUN pip3 install -r requirements.txt

ARG DJANGO_SETTINGS_MODULE=eventex.settings
ARG ALLOWED_HOSTS=127.0.0.1,.localhost,.herokuapp.com

ARG SECRET_KEY=$SECRET_KEY
ARG DEBUG=$DEBUG
ARG ALLOWED_HOSTS=$ALLOWED_HOSTS

RUN flake8 --exclude=eventex/migrations/ eventex/ && python ./manage.py test

CMD gunicorn eventex.wsgi --log-file -
