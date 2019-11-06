import MySQLdb
import time
import os


db_config = {
    'host': 'localhost',
    'port': 3306,
    'db': 'movies',
    'user': 'root',
    'password': '123456'
}


def test_not_close_conn_unnormal_exit():
    print('begin connecting to mysql')
    conn = MySQLdb.Connection(autocommit=True, **db_config)

    # sleep 20s to check the connection
    print('mysql connected. sleeping ...')
    pid = os.getpid()
    print(f'current pid is {pid}, you can kill me now ...')
    time.sleep(2000)

if __name__ == '__main__':
    test_not_close_conn_unnormal_exit()