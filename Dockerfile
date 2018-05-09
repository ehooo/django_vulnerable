FROM python:3

ENV PYTHONUNBUFFERED 1

## INSTALL DEPENDENCES
# FIX -> fatal error: libmemcached/memcached.h: No such file or directory
RUN wget https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz -O libmemcached.tar.gz \
    && tar -zxf libmemcached.tar.gz \
    && cd libmemcached-* \
    && ./configure && make && make install \
    && cd .. \
    && rm -fr libmemcached*

## COPY CODE
RUN mkdir /code
ADD Pipfile /code
ADD django_vulnerable /code/django_vulnerable
ADD vulnerable /code/vulnerable
ADD manage.py /code

## INSTALL CODE
WORKDIR /code

ENV PIPENV_IGNORE_VIRTUALENVS 1
RUN pip install pipenv \
    && pipenv install --deploy

# ENV PYTHONPATH /code/_env/bin/python:/usr/local/bin/python

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
