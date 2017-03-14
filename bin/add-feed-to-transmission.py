#!/usr/bin/env python
#coding=utf-8
"""
Author:         Kent Xia/Xia Kai <kentx@pronto.net/xiaket@gmail.com>
Filename:       add-feed-to-transmission.py
Date created:   2017-03-14 12:10
Last modified:  2017-03-14 14:07
Modified by:    Kent Xia/Xia Kai <kentx@pronto.net/xiaket@gmail.com>

Description:

Changelog:

"""
import logging
from datetime import datetime, timedelta

import feedparser


TV_SERIES = [
    'the walking dead',
    'the big bang theory',
    'legion',
    'homeland',
    'family guy',
]

logging.basicConfig(
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='/data/var/log/feed-parser.log',
    format='%(asctime)s %(message)s',
    level=logging.DEBUG,
)

def read_url():
    with open('/data/etc/torrentleech.url') as fobj:
        return fobj.read().strip()

def get_recent_items(url):
    # return a list of new items from the RSS.
    # by new, we mean published within the last xx minutes.
    recent = timedelta(minutes=121)
    deadline = datetime.utcnow() - recent

    parsed = feedparser.parse(url)
    items = []
    dt_format = "%a, %d %b %Y %H:%M:%S +0000"
    for entry in parsed.entries:
        published = datetime.strptime(entry['published'], dt_format)
        if published > deadline:
            logging.debug("Found updated title: %s", entry['title'])
            items.append(entry)
    return items

def select_good_items(items):
    good_items = []
    for item in items:
        for name in TV_SERIES:
            title = item['title'].lower()
            if name in title and '720p' in title:
                logging.debug("Found good title: %s", title)
                good_items.append(item)
        if '720p' in title:
            logging.debug("Found 720p title: %s", title)

    return good_items

def main():
    url = read_url()
    recent_items = get_recent_items(url)
    select_good_items(recent_items)

if __name__ == '__main__':
    main()
