#!/usr/bin/env bash

sudo  gunicorn -k tornado -w 4 -b 0.0.0.0:8888 app:application

