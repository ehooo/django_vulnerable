FROM python:3.6-jessie

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
ADD requirements.txt /code
ADD django_vulnerable /code/django_vulnerable
ADD vulnerable /code/vulnerable
ADD manage.py /code

## INSTALL CODE
WORKDIR /code

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
