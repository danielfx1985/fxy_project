FROM python:3.8-alpine
RUN mkdir "code"
WORKDIR /code
COPY rq.txt /code/
RUN pip install -r rq.txt
COPY . /code