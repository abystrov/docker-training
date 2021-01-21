FROM python:3.7-alpine

WORKDIR /app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install pipenv psycopg2

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system

COPY app .
# RUN pipenv shell

CMD gunicorn --bind=0.0.0.0 -w4 simple:app
