FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

RUN pip install pipenv

COPY python-fastapi-app/Pipfile python-fastapi-app/Pipfile.lock /code/

RUN set -ex && pipenv install --system --dev

COPY python-fastapi-app /code/

EXPOSE 8000