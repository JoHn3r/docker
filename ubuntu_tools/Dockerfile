FROM python:3

RUN mkdir /home_dir && mkdir /workspace

RUN apt update && apt upgrade && apt install --assume-yes curl tcpdump docker openrc ansible jq realmd

RUN pip3 install awscli --upgrade --user

WORKDIR /home_dir

ENTRYPOINT [ "/bin/sh","-c" ]


