# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'
<<<<<<< HEAD
=======


from config import Config
from redis import Redis

import json

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def pg_conn():
    engine = create_engine(Config.db)
    Session = sessionmaker(engine)
    session = Session()
    return session


def redis_conn():
    conn = Redis(host=Config.redis_db.get("host"),
                 port=Config.redis_db.get("port"))
    return conn
>>>>>>> 85e7424cf14daa2d8af9040031bec995ac70cde1
