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

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]

CMD gunicorn eventex.wsgi --log-file -