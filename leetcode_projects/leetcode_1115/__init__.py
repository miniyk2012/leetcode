import threading
from threading import Lock
from typing import Callable

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock2.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.lock1.acquire()
            printFoo()
            self.lock2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.lock2.acquire()
            printBar()
            self.lock1.release()


def run_cases(i):
    foobar = FooBar(i)
    threads = []
    threads.append(threading.Thread(target=foobar.foo, args=[lambda: print('foo'), ]))
    threads.append(threading.Thread(target=foobar.bar, args=[lambda: print('bar'), ]))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    run_cases(5)
