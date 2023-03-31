FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

RUN pip install pipenv

COPY python-starlette-app/Pipfile python-starlette-app/Pipfile.lock /code/

RUN set -ex && pipenv install --system --dev

COPY python-starlette-app /code/

EXPOSE 8000