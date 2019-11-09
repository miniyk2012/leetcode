import threading
import time
from threading import Lock


def generator():
    for i in range(3):
        time.sleep(1)
        yield i


g = generator()
lock = Lock()


def do(g):
    with lock:
        for x in g:
            print(x)


for _ in range(2):
    t = threading.Thread(target=do, args=(g,))
    t.start()
