FROM python:3.9.5-alpine

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN addgroup -S app && adduser -h /home/app -s /bin/bash -D -u 2000 app -G app

WORKDIR /home/app

RUN apk add postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN python -m pip install --upgrade pip

COPY requirements.txt /home/app

RUN pip install -r requirements.txt --default-timeout=100 --no-cache

RUN pip install gunicorn

COPY . /home/app
RUN chown -R app:app /home/app
USER app
RUN python manage.py collectstatic --no-input -c


ENTRYPOINT ["/home/app/entrypoint.sh"]