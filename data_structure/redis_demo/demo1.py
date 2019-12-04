import redis  # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

pool = redis.ConnectionPool(host='localhost', port=6379,
                            decode_responses=True)  # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379

r = redis.Redis(connection_pool=pool)


def batch_lpop(key, n):
    p = r.pipeline()
    p.lrange(key, 0, n - 1)
    p.ltrim(key, n, -1)
    data = p.execute()
    return data


r.rpush('l1', *list(range(100)))
z = batch_lpop('l1', 10)
print(z)
