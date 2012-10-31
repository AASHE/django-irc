#!/bin/sh
# Cron script to perform link checking on aashe-rc

export DJANGO_SETTINGS_MODULE=rc.live_settings
SITE_ROOT=/var/www/django_projects/aashe-rc

source $SITE_ROOT/env/bin/activate
$SITE_ROOT/current/rc/manage.py findlinks
$SITE_ROOT/current/rc/manage.py checklinks
