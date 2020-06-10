import threading
import time

import redis

conn = redis.StrictRedis(host="localhost", port=6379, db=1)
conn.mset({'a_num': 10, 'b_num': 10})


def a_to_b():
    pipeline = conn.pipeline()
    try:
        pipeline.watch('a_num')
        if int(conn.get('a_num')) < 10:
            print('a_num < 10')
            pipeline.unwatch()
            return
        pipeline.multi()
        pipeline.decr('a_num', 10)
        # time.sleep(.1)
        pipeline.incr('b_num', 10)
        pipeline.execute()
        print(conn.mget('a_num', "b_num"))
    except redis.exceptions.WatchError as e:
        print(e)
        pass


def b_to_a():
    pipeline = conn.pipeline()
    try:
        pipeline.watch('b_num')
        if int(conn.get('b_num')) < 10:
            print('b_num < 10')
            pipeline.unwatch()
            return
        pipeline.multi()
        pipeline.decr('b_num', 10)
        # time.sleep(.1)
        pipeline.incr('a_num', 10)
        pipeline.execute()
        print(conn.mget('a_num', "b_num"))
    except redis.exceptions.WatchError as e:
        print(e)
        pass


if __name__ == '__main__':
    pool = [threading.Thread(target=a_to_b) for i in range(3)]
    for t in pool:
        t.start()

    pool = [threading.Thread(target=b_to_a) for i in range(3)]
    for t in pool:
        t.start()
