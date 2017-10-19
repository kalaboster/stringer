#!/usr/bin/env bash
sudo rm /etc/nginx/sites-enabled/default

sudo ln -s /var/www/stringer/install/stringer_nginx.conf /etc/nginx/conf.d/



sudo service nginx restart


sudo mkdir -p /var/log/uwsgi
sudo chown -R ubuntu:ubuntu /var/log/uwsgi
uwsgi --ini /var/www/stringer/install/stringer_uwsgi.ini