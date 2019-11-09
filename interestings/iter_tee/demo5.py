import itertools
import threading


def generator():
    for i in range(1000000):
        yield i


g = generator()

class SafeTee:
    def __init__(self, tee, lock):
        self.tee_obj = tee
        self.lock = lock

    def __next__(self):
        with self.lock:
            return next(self.tee_obj)

    def __iter__(self):
        return self


def safe_tee(g, n):
    """线程安全的tee"""
    lock = threading.Lock()
    return tuple(SafeTee(tee_obj, lock) for tee_obj in itertools.tee(g, n))

for x in safe_tee(g, 10):
    t = threading.Thread(target=lambda x: print(sum(x)), args=(x,))
    t.start()

