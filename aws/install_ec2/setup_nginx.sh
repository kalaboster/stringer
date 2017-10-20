#!/usr/bin/env bash

sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /var/www/service/stringer/aws/install_ec2/stringer_nginx.conf /etc/nginx/sites-enabled/
sudo service nginx restart
sudo service uwsgi restart