FROM python:3.7

RUN mkdir /eventex
WORKDIR /eventex
COPY ./requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev &&  \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/archive/*.deb

COPY . .

ENV DJANGO_SETTINGS_MODULE=eventex.settings
ENV ALLOWED_HOSTS=$ALLOWED_HOSTS
ENV DEBUG=$DEBUG
ENV SECRET_KEY=$SECRET_KEY
ENV EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
ENV EMAIL_HOST=localhost
ENV EMAIL_PORT=25
ENV EMAIL_USE_TLS=True
ENV EMAIL_HOST_USER=
ENV EMAIL_HOST_PASSWORD=

RUN pip install flake8 && flake8 --exclude=eventex/migrations/ eventex/ && python manage.py test

CMD gunicorn eventex.wsgi --log-file -
