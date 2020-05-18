FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements/ /code/requirements/

RUN pip install -r requirements/production.txt
COPY . /code/

CMD uvicorn config.asgi:application
