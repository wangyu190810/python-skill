from sqlalchemy import create_engine
from functools import wraps
import time

def run_time(func):

    #def _run_time(func):
        # import functools
        # @functools.wraps(func)
        # def _wrapper(*args, **kwargs):
        #     arg = 'call'
        #     try:
        #         pass
        #         #func(*args, **kwargs)
        #     finally:
        #         end_time = time.time()
        #         exe_time = start - end_time
        #         print exe_time
        # return _wrapper
        # #
    @wraps(func)
    def _wraps(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        exe_time = end_time - start
        print exe_time
    return _wraps

def conn():
    engin = create_engine("mysql://root:@localhost:3306/test")
    return engin


def queryone(sql):
    db = conn()
    stmt = db.execute(sql)
    #db.close()
    return stmt.fetchone()

#@run_time
def queryall(sql):
    db = conn()
    stmt = db.execute(sql)
    #db.close()
    return stmt.fetchall()
