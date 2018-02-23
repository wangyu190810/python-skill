# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'

import tornado.ioloop
import tornado.web
import time
from threading import local, Thread,currentThread
import json
import os


user = local()

if not os.environ.has_key('_BASIC_PATH_'):
    _BASIC_PATH_ = os.path.abspath(__file__)
    _BASIC_PATH_ = _BASIC_PATH_[:_BASIC_PATH_.rfind('/bin/')]
    os.environ['_BASIC_PATH_'] = _BASIC_PATH_
else:
    _BASIC_PATH_ = os.environ['_BASIC_PATH_']

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous

    def get(self):
        time.sleep(5)
        self.write("Hello, world")
        self.finish()

class AppHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        #time.sleep(10)
        app = {
            "username":"你好"
        }
        self.write(json.dumps(app))
        self.finish()


class TestThread(Thread):
    def run(self):
        print(currentThread())

#
# class ThreadHandler(tornado.web.RequestHandler):
#     user.t = TestThread()
#     def get(self):
#         user._name = "tom"
#         data = {"name":user._name}
#         user.name = data.get("name")
#         #self.write("hello :%s"%(user.name))
#         user.count = dir(bind_user)
#         user.count_num = bind_user.count()
#         #user.age = bind_user.age()
#
#         user.t.start()
#         user.t.join()
#
#         self.write("hello :%s,count :%s"%(user.name,user.count_num))
#



def make_app():
    a = tornado.web.Application([
            #(r"/", MainHandler),
            (r"/app",AppHandler),
            (r"/(.*)",tornado.web.StaticFileHandler,{"path": _BASIC_PATH_ + "/static/"})
            #(r"/user",ThreadHandler)
        ],debug=True)
    return a

if __name__ == "__main__":
    application = make_app()
    application.listen(9898)
    tornado.ioloop.IOLoop.current().start()
