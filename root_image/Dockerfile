FROM python:3-alpine

RUN echo http://dl-cdn.alpinelinux.org/alpine/latest-stable/community/ >> /etc/apk/repositories
RUN mkdir /home_dir && mkdir /workspace
RUN apk update && apk upgrade && apk --no-cache add sudo curl tcpdump docker openrc
RUN pip3 install docker-compose flask

COPY ./Flask/app.py /workspace/app.py
COPY ./Flask/docker-entrypoint.sh /workspace/docker-entrypoint.sh



