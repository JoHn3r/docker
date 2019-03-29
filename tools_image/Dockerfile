FROM python:3-alpine

RUN echo http://dl-cdn.alpinelinux.org/alpine/latest-stable/community/ >> /etc/apk/repositories

RUN mkdir /home_dir && mkdir /workspace

RUN apk update && apk upgrade && apk --no-cache add sudo curl tcpdump docker openrc ansible jq

WORKDIR /home_dir

ENTRYPOINT [ "/bin/sh","-c" ]


