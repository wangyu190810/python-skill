# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'

import requests
from lib import create_log
import logging

from db import insert_data


def count_worlds_at_url(url):
    resp = requests.get(url,timeout=2)
    create_log(log_name="url")
    data = {"url":url,""
                      "status_code":resp.status_code}
    insert_data(data)
    logging.info(resp.status_code)
    if resp.status_code != 200:
        return url


