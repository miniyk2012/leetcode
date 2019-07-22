import threading
from threading import Lock
from typing import Callable


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.even_num = 2
        self.odd_num = 1
        self.total_num = 0
        self.even_lock = Lock()
        self.even_lock.acquire()
        self.odd_lock = Lock()
        self.odd_lock.acquire()
        self.zero_lock = Lock()

    def done(self):
        return self.total_num >= 2 * self.n

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while not self.done():
            self.zero_lock.acquire()
            if self.done():
                self.odd_lock.release()
                self.even_lock.release()
                break
            printNumber(0)
            self.total_num += 1
            if self.total_num % 4 == 3:
                self.even_lock.release()
            elif self.total_num % 4 == 1:
                self.odd_lock.release()
            else:
                raise RuntimeError('不应该发生')

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while not self.done():
            self.even_lock.acquire()
            if self.done():
                self.zero_lock.release()
                break
            printNumber(self.even_num)
            self.even_num += 2
            self.total_num += 1
            self.zero_lock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while not self.done():
            self.odd_lock.acquire()
            if self.done():
                self.zero_lock.release()
                break
            printNumber(self.odd_num)
            self.odd_num += 2
            self.total_num += 1
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
