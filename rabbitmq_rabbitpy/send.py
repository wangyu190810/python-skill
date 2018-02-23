# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'

import rabbitpy
from config import Config

from lib import rabbit_conn

with rabbit_conn(Config.rabbitmq).channel() as channel:
    queue = rabbitpy.Queue(channel, 'example')
    queue.durable = True
    queue.declare()

with rabbit_conn(Config.rabbitmq).channel() as channel:
    message = rabbitpy.Message(channel,"message")
    if message.publish("test_example","test_routing-key",mandatory=True):
        print("message publish")
    else:
        print("rabbitmq indicates message publishing failure")

    # for message in rabbitpy.Queue(channel, 'example'):
    #     print 'Message: %r' % message
    #     message.ack()
    #
