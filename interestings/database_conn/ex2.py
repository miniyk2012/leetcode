"""https://www.jianshu.com/p/bf22299f2a9a
MySQL数据库连接的相关探索"""


import sys
import threading
import time

import MySQLdb
# 注意这里PersistentDB是在PersistentDB Module当中
from DBUtils.PersistentDB import PersistentDB

db_config = {
    'host': 'localhost',
    'port': 3306,
    'db': 'movies',
    'user': 'root',
    'password': '123456'
}


db_persis = PersistentDB(
    # creator即你使用的db driver
    creator=MySQLdb,
    # 如果在支持threading.local的环境下可以使用如下配置方式，性能更好
    threadlocal=threading.local,
    **db_config
)


def test_with_dbutils_persistent_conn():
    print('begin connecting to mysql')
    conn = db_persis.connection()

    print('after get connection, sleep 100s')
    time.sleep(5)

    # 这里close并没有真正关闭数据库的connection
    # 而是被PersistentDB回收
    conn.close()
    print('close function already called, sleep 100s again')

    time.sleep(5)
    sys.exit()


if __name__ == '__main__':
    test_with_dbutils_persistent_conn()
