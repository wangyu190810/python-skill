# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'

import logging
from config import Config


def create_log(log_name):
    logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%m-%d %H:%M',
            filename=Config.log_folder+log_name+".log",
            filemode='w'
    )

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
