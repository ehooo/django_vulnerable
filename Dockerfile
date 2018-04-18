FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
ADD . /code
WORKDIR /code

RUN pipenv install

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
