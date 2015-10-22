#!/bin/sh

if [ `date +%H` == "05" ]
then
    python ~/app-root/repo/manage.py shell < ~/app-root/repo/inputdb.py
fi