FROM ubuntu

RUN apt update && apt install -y curl tcpdump openrc ansible jq realmd iputils-ping dnsutils

RUN pip3 install awscli --upgrade --user

ENTRYPOINT [ "/bin/sh","-c" ]


