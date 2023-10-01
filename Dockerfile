FROM python:3.9.18-slim-bullseye

LABEL com.since="0.0.1"

EXPOSE 8000

ARG env

WORKDIR /

# Build the logging structure
RUN mkdir -p /logging/
RUN mkdir -p /logging/gunicorn/

RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY eval_env.sh \
    wf_list_urls_django.sh \
    wf_run_django.sh \
    wf_run_migration_django.sh \
    wf_run_test_django.sh \
    gunicorn_run.sh ./

COPY source/ source/
RUN ./wf_run_migration_django.sh $env


ENTRYPOINT [ "/bin/bash" ]