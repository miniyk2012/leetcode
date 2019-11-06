import MySQLdb
import time
import threading
import os
from DBUtils.PersistentDB import PersistentDB
from DBUtils.PooledDB import PooledDB
import sys

db_config = {
    'host': 'localhost',
    'port': 3306,
    'db': 'movies',
    'user': 'root',
    'password': '123456'
}


db_pool = PooledDB(
    creator=MySQLdb,
    mincached=2,
    maxconnections=35,
    blocking=True,
    maxcached=10,
    **db_config
)


def test_with_pooleddb_conn():
    def new_conn(i):
        conn = db_pool.connection()
        print(f'{i} begin connecting to mysql')
        time.sleep(10)
        print(f'after get connection, ${i} sleep 100s')
        conn.close()
    threads = []
    for i in range(50):
        t = threading.Thread(target=new_conn, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('all conn close')
    time.sleep(50)

    print('program exit')




if __name__ == '__main__':
    test_with_pooleddb_conn()