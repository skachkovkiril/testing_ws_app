FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

RUN pip install pipenv

COPY python-asyncio-app/Pipfile python-asyncio-app/Pipfile.lock /code/

RUN set -ex && pipenv install --system --dev

COPY python-asyncio-app /code/

EXPOSE 8000

CMD ["python", "main.py"]