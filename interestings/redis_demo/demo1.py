import threading
import time

import redis

conn = redis.StrictRedis(host="localhost", port=6379, db=1)
conn.mset({'a_num':10, 'b_num':10})


def a_to_b():
    if int(conn.get('a_num')) >= 10:
        conn.decr('a_num', 10)
        time.sleep(.1)
        conn.incr('b_num', 10)
    print(conn.mget('a_num', "b_num"))


def b_to_a():
    if int(conn.get('b_num')) >= 10:
        conn.decr('b_num', 10)
        time.sleep(.1)
        conn.incr('a_num', 10)
    print(conn.mget('a_num', "b_num"))


if __name__ == '__main__':
    pool = [threading.Thread(target=a_to_b) for i in range(3)]
    for t in pool:
        t.start()

    pool = [threading.Thread(target=b_to_a) for i in range(3)]
    for t in pool:
        t.start()