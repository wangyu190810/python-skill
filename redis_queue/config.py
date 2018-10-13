# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'


class Config(object):
    log_folder = "."
    db = "postgresql+psycopg2://user:password@host:port/test"
    redis_db = {"host":"121.40.87.224","port":6379}
