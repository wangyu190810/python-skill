# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'
<<<<<<< HEAD
=======
from functools import wraps
import json

from lib import redis_conn,pg_conn


def set_cache(key,values):
    redis_conn().set(key,values,ex=10)
    return True


def get_cache(key):
    data = redis_conn().get(key)
    print data
    return data


def get_pg_index(sql):
    stmt = pg_conn().execute(sql).fetchone()
    index = dict()
    index[stmt[0]] = stmt
    return index
>>>>>>> 85e7424cf14daa2d8af9040031bec995ac70cde1
