import time
import threading
from typing import List, Callable


class Foo:

    def __init__(self):
        self.locks = (threading.Lock(), threading.Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.locks[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.locks[0]:
            printSecond()
        self.locks[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.locks[1]:
            printThird()


def pick_run(foo: Foo, i):
    if i == 1:
        foo.first(lambda: print('first'))
    elif i == 2:
        foo.second(lambda: print('second'))
    elif i == 3:
        foo.third(lambda: print('third'))
    else:
        raise Exception('Error')


class Solution:
    def foobar(self, nums: List[int]) -> None:
        foo = Foo()
        for i in nums:
            threading.Thread(target=pick_run, args=(foo, i,)).start()


if __name__ == "__main__":
    s = Solution()
    s.foobar([2, 3, 1])
    time.sleep(1)
    print()
    s.foobar([1, 3, 2])
