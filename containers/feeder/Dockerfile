FROM python:alpine

MAINTAINER Kai Xia(xiaket@gmail.com)

RUN pip install requests feedparser
COPY feeder.py /feeder

VOLUME /var/torrents /var/feeder

ENTRYPOINT ["/feeder"]
