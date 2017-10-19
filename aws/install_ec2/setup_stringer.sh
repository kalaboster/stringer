#!/usr/bin/env bash

pip install -r requirements.txt
mkdir /var/www
mkdir /var/www/stringer
cp -R . /var/www/stringer/
chown -R ubuntu:ubuntu /var/www/stringer

