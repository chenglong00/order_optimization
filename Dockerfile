FROM python:3.10

MAINTAINER Chenglong Wu <chenglong.w1@gmail.com>

RUN apt-get update && \
    apt-get install -y python-dev python3-pip build-essential libxml2-dev libxslt1-dev zlib1g-dev

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD ./requirements.txt /code/requirements.txt
ADD ./order_optimizer /code/order_optimizer
ADD ./tests /code/tests

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV PYTHONPATH=/code/order_optimizer

# Running test
RUN python -m unittest discover -p test*.py -v

CMD ["uvicorn", "order_optimizer.api.main:app", "--reload", "--workers", "1",  "--host", "0.0.0.0", "port", "8080"]
