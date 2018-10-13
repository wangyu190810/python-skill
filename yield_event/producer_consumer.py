# -*-coding:utf-8-*-

import random

def get_data():
    """随机返回三个数值"""
    return random.sample(range(10),3)


def consume():
    """"""
    runing_sum = 0
    data_items_seen = 0

    while True:
        print("Waiting to consume")
        data = yield
        print(data)
        data_items_seen += len(data)
        runing_sum = sum(data)
        print("consumeed ,the runing average is %s"%(runing_sum/float(data_items_seen)))

def produce(consumer):

    while True:
        data = get_data()
        print("Product data is :%s"%data)
        consumer.send(data)
        yield

if __name__ == "__main__":
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)

    for _ in range(10):
        print("Producing")
        next(producer)
