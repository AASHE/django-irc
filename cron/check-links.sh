#!/bin/sh
# Cron script to perform link checking on aashe-rc
# on the production server

DJANGO_SETTINGS_MODULE=live_settings
SITE_ROOT=/var/www/django_projects/aashe-rc
VIRTUALENV=$SITE_ROOT/env/bin/python

$VIRTUALENV $SITE_ROOT/current/rc/manage.py findlinks --settings=$DJANGO_SETTINGS_MODULE
$VIRTUALENV $SITE_ROOT/current/rc/manage.py checklinks --settings=$DJANGO_SETTINGS_MODULE
