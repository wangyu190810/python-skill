# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'

from  sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,text

from config import Config


def connection(database):
    engine = create_engine(database)
    Session = sessionmaker(engine)
    session = Session()
    return session

conn = connection(Config.db)


def insert_data(data):
    sql =text("insert into queue_message (url,status_code) "
              "VALUES (:url,:status_code)")
    sql = sql.bindparams(url=data.get("url"),
                         status_code=data.get("status_code"))
    conn.execute(sql)
    conn.commit()
