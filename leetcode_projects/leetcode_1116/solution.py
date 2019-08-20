import threading
from threading import Lock
from typing import Callable


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.odd_lock = Lock()
        self.odd_lock.acquire()
        self.even_lock = Lock()
        self.even_lock.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: Callable[[int], None]) -> None:
        for _ in range(self.n):
            self.zero_lock.acquire()
            printNumber(0)
            if _ % 2 == 0:
                self.odd_lock.release()
            else:
                self.even_lock.release()

    def even(self, printNumber: Callable[[int], None]) -> None:
        for i in range(2, self.n + 1, 2):
            self.even_lock.acquire()
            printNumber(i)
            self.zero_lock.release()

    def odd(self, printNumber: Callable[[int], None]) -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()


def run_cases(i):
    foobar = ZeroEvenOdd(i)

    def printNumber(i):
        print(i)

    threads = []
    threads.append(threading.Thread(target=foobar.odd, args=[printNumber, ]))
    threads.append(threading.Thread(target=foobar.zero, args=[printNumber, ]))
    threads.append(threading.Thread(target=foobar.even, args=[printNumber, ]))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    run_cases(11)
