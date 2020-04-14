FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y libpq-dev \
  && apt-get install -y python3-pip python3-dev curl python3-psycopg2 \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
