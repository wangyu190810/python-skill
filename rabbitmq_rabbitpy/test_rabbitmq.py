# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'

import rabbitpy

# with rabbitpy.Connection("amqp://guest:guest@localhost:5672/%2F") as conn:
#     with conn.channel() as channel:
#         amqp = rabbitpy.AMQP(channel)
#
#         for message in amqp.basic_consume('queue-name'):
#             print(message)
#
# import rabbitpy

with rabbitpy.Connection('amqp://guest:guest@localhost:5672/%2f') as conn:
    with conn.channel() as channel:
        queue = rabbitpy.Queue(channel, 'example')

        while len(queue) > 0:
            message = queue.get()
            print 'Message:'
            print ' ID: %s' % message.properties['message_id']
            print ' Time: %s' % message.properties['timestamp'].isoformat()
            print ' Body: %s' % message.body
            message.ack()

            print 'There are %i more messages in the queue' % len(queue)