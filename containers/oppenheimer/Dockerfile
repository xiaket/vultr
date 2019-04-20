FROM alpine:latest

MAINTAINER Kai Xia(xiaket@gmail.com)

RUN apk add --update \
    transmission-daemon wget \
    && rm -rf /var/cache/apk/* \
    && wget -O- https://api.github.com/repos/ronggang/transmission-web-control/releases/latest \
        | grep tarball_url | cut -d  '"' -f 4 | xargs wget -O /tmp/twc.tgz \
    && tar xfz /tmp/twc.tgz \
    && mkdir /tmc \
    && mv /ronggang-transmission-web-control-*/src/* /tmc/ \
    && rm -rf /ronggang-transmission-web-control-* /tmp/twc.tgz

VOLUME /transmission/downloads /transmission/watch /transmission/incomplete /var/transmission-daemon

EXPOSE 51413/tcp 51413/udp 9091/tcp

CMD ["/usr/bin/transmission-daemon", "--foreground", "--config-dir", "/var/transmission-daemon"]
