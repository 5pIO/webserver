#!/bin/sh
# webserver_launcher.sh
# This script goes to the webserver directory and starts it using python

cd /home/pi/webserver
sudo python simpleserver.py
cd /