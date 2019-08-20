from multiprocessing.dummy import Pool as ThreadPool


def test(*_):
    print('hello')


if __name__ == '__main__':
    pool = ThreadPool(3)
    ret = pool.map(test, (1, ))
    print(ret)
