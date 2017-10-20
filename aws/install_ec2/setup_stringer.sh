#!/usr/bin/env bash

# Install the requirements.
sudo pip install -r /var/www/service/stringer/requirements.txt
sudo ln -s /var/www/service/stringer/aws/install_ec2/stringer_uwsgi.ini /etc/uwsgi/apps-enabled/




