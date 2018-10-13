# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'
import rabbitpy
from sqlalchemy.pool import QueuePool
from sqlalchemy import create_engine

import logging

from rabbitmq_rabbitpy.config import Config


def rabbit_conn(rabbit_url):
    conn = rabbitpy.Connection(rabbit_url)
    return conn


def pg_conn(database):
    conn = create_engine(database,poolclass=QueuePool)
    return conn.connect()


def create_log(log_name):
    logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%m-%d %H:%M',
            filename=Config.log_folder+log_name+".log",
            filemode='a'
    )

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

