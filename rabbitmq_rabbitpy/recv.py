# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'

import rabbitpy

from lib import rabbit_conn
from config import Config


with rabbit_conn(Config.rabbitmq).channel() as channel:
    queue = rabbitpy.Queue(channel, 'example')
    for message in queue.consume():
        print 'Message: %r' % message
        message.ack()