#!/usr/bin/env python
# -*-coding:utf-8-*-
import os,sys
import time
# async def ping(ping_id:int):
def ping(ping_id: int):

    ping_data = os.system('ping www.baidu.com')
    print(ping_data.bit_length())
    print(ping_id)

def run():
    for row in range(3):
        ping(row)

if __name__ == '__main__':
    run()
    while True:
        time.sleep(0.5)
