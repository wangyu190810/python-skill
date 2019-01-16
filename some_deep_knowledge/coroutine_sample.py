#!/usr/bin/env python
# -*-coding:utf-8-*-
import select
import socket


def coroutine():
    sock = socket.socket()
    sock.setblocking(0)
    print("set")
    address = yield sock
    try:
        sock.connect(address)
    except BlockingIOError:
        print(BlockingIOError)
        pass
    data = yield
    print("data %s" %data)
    size = yield sock.send(data)
    print(size)
    yield sock.recv(size)


def main():
    coro = coroutine()
    print("coro")
    sock = coro.send(None)
    print("send None")
    wait_list = (sock.fileno(),)
    print(coro.send(('www.baidu.com', 80)))
    print("send 80")
    select.select((), wait_list, ())
    print("select ")
    print(coro.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: Close\r\n\r\n'))
    select.select(wait_list, (), ())
    print(coro.send(1024))

if __name__ == '__main__':
    main()
