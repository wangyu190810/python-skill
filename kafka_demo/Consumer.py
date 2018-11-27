#!/usr/bin/env python
# -*-coding:utf-8-*-
from kafka import KafkaConsumer
import ujson
consumer = KafkaConsumer('test_rhj', bootstrap_servers='192.168.1.11:9092')
for msg in consumer:
    print(msg.value)
    # recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    # print recv
    data = ujson.loads(msg.value)
    # print(type(data))
    # print(data['sleep_time'])