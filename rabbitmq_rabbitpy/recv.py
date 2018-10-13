# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'
<<<<<<< HEAD
=======

import rabbitpy

from lib import rabbit_conn
from config import Config


with rabbit_conn(Config.rabbitmq).channel() as channel:
    queue = rabbitpy.Queue(channel, 'example')
    for message in queue.consume():
        print 'Message: %r' % message
        message.ack()
>>>>>>> 85e7424cf14daa2d8af9040031bec995ac70cde1
