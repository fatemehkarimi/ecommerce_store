#pull base image
FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#add line below when running pipenv install
ENV PIP_NO_CACHE_DIR 0

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN python3 -m pip install pipenv && pipenv install --system

COPY . /code/