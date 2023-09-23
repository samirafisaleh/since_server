FROM python:3.9.18-slim-bullseye

LABEL com.since="0.0.1"

EXPOSE 8000

ARG env

WORKDIR /

COPY django_run.sh gunicorn_run.sh django_run_migration.sh ./

# Build the logging structure
RUN mkdir -p /logging/
RUN mkdir -p /logging/gunicorn/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY source/ source/
RUN ./django_run_migration.sh $env


ENTRYPOINT [ "/bin/bash" ]