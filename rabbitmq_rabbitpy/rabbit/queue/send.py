# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'


import rabbitpy

from lib.lib import rabbit_conn


with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        queue = rabbitpy.Queue(channel, 'my-queue')
        queue.durable = True
        queue.declare()

with conn.channel() as channel:
    for message in rabbitpy.Queue(channel, 'example'):
        print 'Message: %r' % message
        message.ack()