from base import queryone,queryall,run_time

import threading
import gevent
from functools import wraps
import time
import multiprocessing



data = None
icallback = {}



    #return _run_time


def asyn_callback(sql):
    #global icallback
    data = queryall(sql)
    icallback[sql] = data

def callback_data(sql):
    #global icallback
    while 1:
        data = icallback.get(sql)
        if data:
            del icallback[sql]
            break
    return data

def query_data(sql,callback_data=None,callback=None):
    callback(sql)
    return callback_data(sql)

@run_time
def task(sql):
    data = query_data(sql,callback_data,asyn_callback)
    return data

@run_time
def asynchronous_event():
    # sql = "select * from email limit %s"
    #
    # threads = [gevent.spawn(task,sql%i) for i in range(1,10**6,10**4)]
    #print threads
    sql = "select * from email"
    threads = [gevent.spawn(task,sql) for i in range(4)]
    gevent.joinall(threads)

@run_time
def asynchronous_multiprocessing():
    record = []
    sql = "select * from email"
    for i in range(4):
        process = multiprocessing.Process(target=task,args=(sql,))
        process.start()
        record.append(process)
    for row in record:
        process.join()



@run_time
def synchronous():
    sql = "select * from email limit %s"
    sql = "select * from email"
    for i in range(4):
        start = time.time()
        #queryall(sql%i)
        queryall(sql)
        end = time.time()
        print(end - start)



if __name__=="__main__":
    #data = query_data(callback_data,asyn_callback)
    #print data
    #print  icallback
    # asynchronous_event()
    # synchronous()
    asynchronous_multiprocessing()
