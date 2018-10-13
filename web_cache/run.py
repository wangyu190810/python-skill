# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'
<<<<<<< HEAD

from flask import Flask

app =
=======
from gevent import monkey
monkey.patch_socket()


from gevent.pywsgi import WSGIServer
from flask import Flask
from sqlalchemy import text
import time
import json

from lib import pg_conn
from db import get_cache,set_cache,get_pg_index

app = Flask(__name__)

@app.route("/")
def index():
    sql = text("SELECT * FROM study")
    stmt = get_pg_index(sql)
    for key,values in stmt.iteritems():
        set_cache(key,values)
    time.sleep(10)
    return "key set"


@app.route("/cache")
def cache():
    return get_cache("394")

@app.route("/cache_update/<key>")
def update(key):
    stmt = get_cache(key)
    if stmt is None:
        set_cache(key,10086)
        return "set success"
    else:
        return get_cache(key)

if __name__ == "__main__":
    http = WSGIServer(('', 5000), app)
    http.serve_forever()
>>>>>>> 85e7424cf14daa2d8af9040031bec995ac70cde1
