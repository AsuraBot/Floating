FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

ENV DEBUG=0

COPY ./requirements.txt /requirements.txt

# RUN python -m pip install -U --force-reinstall pip

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app
