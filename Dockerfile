FROM python:slim-bullseye

EXPOSE 8000

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY source/ /source/

RUN mkdir -p /logging/

WORKDIR /source/project/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

