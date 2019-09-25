FROM python:3.7 AS Base
COPY ./ /eventex
WORKDIR /eventex
RUN pip3 install -r requirements-dev.txt
RUN pip install flake8
ARG DJANGO_SETTINGS_MODULE=server.settings
ENV SECRET_KEY=$SECRET_KEY

# ------------------------------------------
# Lint
# ------------------------------------------
# FROM Base AS Lint
# RUN pip install flake8
# RUN flake8 --exclude=eventex/migrations/ eventex/


# ------------------------------------------
# Test
# ------------------------------------------
# FROM Base AS Test
# RUN python manage.py test eventex
