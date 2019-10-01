FROM python:3.7

RUN mkdir /eventex
WORKDIR /eventex
COPY ./requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev &&  \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/archive/*.deb

RUN pip3 install -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=eventex.settings
ENV ALLOWED_HOSTS=$ALLOWED_HOSTS
ENV DEBUG=$DEBUG
ENV SECRET_KEY=$SECRET_KEY

CMD gunicorn eventex.wsgi --log-file -