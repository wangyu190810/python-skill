# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'

import requests
from lib import create_log
import logging


def count_worlds_at_url(url):
    resp = requests.get(url)
    create_log(log_name="url")
    logging.info(resp.status_code)
    if resp.status_code != 200:
        return url


