#!/bin/bash

ACME='/data/var/lib/acme/acme.sh --home /data/var/lib/acme --config-home /data/var/lib/acme/data --cert-home /data/var/lib/acme/certs'

# $ACME --issue --dns dns_gd -d torrent.xiaket.org
# $ACME --issue --dns dns_gd -d blog.xiaket.org
# $ACME --issue --dns dns_gd -d d.xiaket.org

$ACME --install-cert -d blog.xiaket.org --keypath /data/etc/ssl/blog.xiaket.org.key --fullchainpath /data/etc/ssl/blog.xiaket.org.crt --reloadcmd  "service blog restart"
$ACME --install-cert -d torrent.xiaket.org --keypath /data/etc/ssl/torrent.xiaket.org.key --fullchainpath /data/etc/ssl/torrent.xiaket.org.crt --reloadcmd  "service transmission restart"
$ACME --install-cert -d d.xiaket.org --keypath /data/etc/ssl/d.xiaket.org.key --fullchainpath /data/etc/ssl/d.xiaket.org.crt --reloadcmd  "service d restart"
