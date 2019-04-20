#!/usr/bin/env python3
import argparse
import logging
import json
import os
import time

import feedparser
import requests


CONF = "/var/feeder/config.json"
DEST = "/var/torrents"

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def get_conf():
    if not os.path.isdir(os.path.dirname(CONF)):
        logging.info("Creating conf dir")
        os.mkdir(os.path.dirname(CONF))
    if not os.path.isfile(CONF):
        return {}
    with open(CONF) as fobj:
        conf = json.load(fobj)
        logging.info("Loaded conf: %s", conf)
        return conf


def save_conf(conf):
    logging.info("Saving conf: %s", conf)
    with open(CONF, "w") as fobj:
        json.dump(conf, fobj)


def add(link):
    logging.info("Adding link: %s", link)
    conf = get_conf()
    conf[link] = []
    save_conf(conf)


def run():
    conf = get_conf()
    for src, known_hashes in conf.items():
        logging.info("Parsing: %s", src)
        items = feedparser.parse(src)
        logging.info("Found %s entries in %s", len(items["entries"]), src)
        if len(items["entries"]) == 0:
            return
        for entry in items["entries"]:
            logging.info("Parsing entry: %s", entry)
            if entry["id"] in known_hashes:
                continue
            logging.info("Adding torrent from: %s", entry)
            for link in entry["links"]:
                if "torrent" not in link["type"]:
                    continue
                logging.info("Downloading torrent: %s", link["href"])
                response = requests.get(link["href"])
                with open(f'{DEST}/{entry["id"]}.torrent', "wb") as fobj:
                    fobj.write(response.content)
                    logging.info("Downloaded torrent: %s", entry["id"])
            conf[src] = list(set(conf[src] + [entry["id"]]))
        save_conf(conf)


def main():
    parser = argparse.ArgumentParser(description="Get torrent in RSS feeds.")
    parser.add_argument("command", choices=["add", "cron", "list", "sleep"])
    parser.add_argument("link", nargs="?")
    parsed = parser.parse_args()
    if parsed.command == "add":
        add(parsed.link)
    elif parsed.command == "list":
        print(json.dumps(get_conf(), indent=2))
    elif parsed.command == "sleep":
        time.sleep(3600)
    else:
        run()


if __name__ == "__main__":
    main()
