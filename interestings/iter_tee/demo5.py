import collections
import itertools
import threading
import time
import types


def generator():
    for i in range(1000000):
        yield i


class SafeTeeIterator:
    def __init__(self, tee, lock):
        self.tee_obj = tee
        self.lock = lock

    def __next__(self):
        with self.lock:
            return next(self.tee_obj)

    def __iter__(self):
        return self


def safe_tee_gen(tee, lock):
    while True:
        with lock:
            try:
                yield next(tee)
            except StopIteration:
                break


def safe_tee(g, n):
    """线程安全的tee"""
    lock = threading.Lock()
    return tuple(SafeTeeIterator(tee_obj, lock) for tee_obj in itertools.tee(g, n))


def safe_tee2(g, n):
    lock = threading.Lock()
    return tuple(safe_tee_gen(tee_obj, lock) for tee_obj in itertools.tee(g, n))


if __name__ == '__main__':
    g1 = generator()
    print(isinstance(g1, collections.abc.Iterator))  # True
    print(isinstance(g1, types.GeneratorType))  # True
    print(type(g1))
    a = enumerate([1, 2, 33])
    print(isinstance(a, collections.abc.Iterator))  # True
    print(isinstance(a, types.GeneratorType))  # False
    print(type(a))
    start = time.time()
    threads = []
    for x in safe_tee2(g1, 10):
        t = threading.Thread(target=lambda x: print(sum(x)), args=(x,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(time.time() - start)

    g2 = generator()
    start = time.time()
    threads2 = []
    for x in safe_tee(g2, 10):
        t = threading.Thread(target=lambda x: print(sum(x)), args=(x,))
        threads2.append(t)
        t.start()
    for t in threads2:
        t.join()
    print(time.time() - start)
