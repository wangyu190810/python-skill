import threading
import Queue
import json
import threading
import sys


if sys.version_info.major > 2:
    import queue
    q = queue.Queue()
else:
    import Queue
    q = Queue.Queue()



def put_value(data):
    q.put_nowait(data)
    print(q.qsize())
    print(threading.currentThread())
    q.join()


def thread_work(cum_num,work,data=()):
    threads = []
    for _ in range(cum_num):
        t= threading.Thread(target=work,args=(data))
        t.start()
        threads.append(t)
    return threads


def work():
    data = q.get_nowait()
    print(data)
    threading.currentThread()
    q.task_done()



if __name__ == "__main__":
    data = {"num":0}
    #for row in range(4):
    # work_threads = thread_work(4,put_value,data)
    # for t in work_threads:
    #     t.join()
    # else:
    #     print("put_value end")

    for row in range(3):
        data["num"] = row
        put_value(data)

    while True:
        work()




    # for _ in range(10):
    #     put_value(data)
    #
    #
    # cum_threads = thread_work(4,work)
    # try:
    #     for i in cum_threads:
    #         t.join()
    # except NameError as e:
    #     print(e)




    # for _ in range(9):
    #     print(pop_value())
