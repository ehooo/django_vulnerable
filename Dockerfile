FROM python:3.4-alpine

ADD . /code
WORKDIR /code

RUN pipenv install

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
