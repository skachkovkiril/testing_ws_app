FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

RUN pip install pipenv

RUN pip install uvloop

COPY python-sanic-app/Pipfile python-sanic-app/Pipfile.lock /code/

RUN set -ex && pipenv install --system --dev

COPY python-sanic-app /code/

EXPOSE 8000

CMD ["python", "main.py"]