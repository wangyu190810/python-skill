#!/usr/bin/env python
# -*-coding:utf-8-*-
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='192.168.1.11:9092')

msg_dict = {
}
data = {"MsgSize": 36, "Filler": "", "PriceLevel": [2], "NoEntries": 1, "MsgType": 53, "UpdateAction": [1],
        "SeqNum": 22805170, "Price": [7650], "AggregateQuantity": [25000], "Side": [1], "NumberOfOrders": [5],
        "SecurityCode": 1800, "SendTime": 1542952376022}
msg_dict = data
print(msg_dict)
msg = json.dumps(msg_dict)
producer.send('test_rhj', msg, partition=0)
producer.close()