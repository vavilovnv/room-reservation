FROM python:3.11

ARG PIP_DISABLE_PIP_VERSION_CHECK=1
ARG PIP_NO_CACHE_DIR=1

WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./.env .
COPY ./alembic.ini .
COPY ./alembic .
COPY ./app ./app