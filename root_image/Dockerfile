FROM alpine:latest

RUN echo http://dl-cdn.alpinelinux.org/alpine/latest-stable/community/ >> /etc/apk/repositories
RUN mkdir /home_dir
RUN apk update && apk upgrade && apk --no-cache add sudo curl python3 tcpdump py-pip docker openrc
RUN pip install docker-compose



