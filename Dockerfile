FROM alpine:latest

MAINTAINER Kai Xia(xiaket@gmail.com)

RUN apk add --update \
    transmission-daemon \
    && rm -rf /var/cache/apk/*

RUN mkdir -p /transmission/downloads \
  && mkdir -p /transmission/incomplete \

VOLUME ["/transmission/downloads"]
VOLUME ["/transmission/incomplete"]
VOLUME ["/etc/transmission-daemon"]

EXPOSE 9091 51413/tcp 51413/udp

ENV USERNAME admin
ENV PASSWORD password

COPY start-transmission.sh .
RUN chmod +x /start-transmission.sh

CMD ["/start-transmission.sh"]
