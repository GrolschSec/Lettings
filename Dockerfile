FROM python:3.10-bullseye

ARG ARG_SECRET_KEY=""

ARG ARG_SENTRY_DSN=""

ENV DJANGO_SECRET=$ARG_SECRET_KEY

ENV SENTRY_DSN=$ARG_SENTRY_DSN

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

RUN python manage.py collectstatic --noinput

EXPOSE 80

CMD [ "gunicorn", "--bind", "0.0.0.0:80", "oc_lettings_site.wsgi" ]
