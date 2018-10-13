# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'
<<<<<<< HEAD
=======

from lib import pg_conn
from sqlalchemy import text

conn = pg_conn()

def insert_data():
    sql = text("INSERT INTO study(name) VALUES (:name)")
    for row in range(10000):
        sql = sql.bindparams(name=str(row)+"key")
        conn.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_data()

>>>>>>> 85e7424cf14daa2d8af9040031bec995ac70cde1
