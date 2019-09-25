FROM python:3.7
COPY ./ /eventex
WORKDIR /eventex

RUN apt-get update && apt-get install -y libpq-dev

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/archive/*.deb

RUN pip3 install -r requirements.txt

ARG DJANGO_SETTINGS_MODULE=server.settings

ENV ALLOWED_HOSTS=$ALLOWED_HOSTS
ENV DEBUG=$DEBUG
ENV SECRET_KEY=$SECRET_KEY

CMD gunicorn eventex.wsgi --log-file -