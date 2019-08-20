from typing import List
import threading
from queue import Queue
import time

class Foo:
    def first(self):
        print("first")

    def second(self):
        print("second")

    def third(self):
        print("third")

foo = Foo()
 
def pick_run(i):
    if i == 1:
        foo.first()
    elif i == 2:
        foo.second()
    elif i == 3:
        foo.third()
    else:
        raise Exception('Error')

class OrderStrategy:
    queue1 = Queue()
    queue2 = Queue()
    queue3 = Queue()

    def __init__(self):
        self.queue1.put(0)

    def order_pick_run(self, i):
        getattr(self, f'queue{i}').get()
        pick_run(i)
        if i < 3:
            getattr(self, f'queue{i+1}').put(0)


class Solution:
    def foobar(self, nums: List[int]) -> int:
        order = OrderStrategy()
        for i in nums:
            threading.Thread(target=order.order_pick_run, args=(i,)).start()

from threading import Barrier

def printFirst():
    print('first')

    
def printSecond():
    print('second')

    
def printThird():
    print('third')


class Foo2:
    """这个方法也很漂亮
    """
    def __init__(self):
        self.first_barrier = Barrier(3)
        self.second_barrier = Barrier(2)
            
    def first(self, printFirst):
        printFirst()
        self.first_barrier.wait()
        
    def second(self, printSecond):
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()
            
    def third(self, printThird):
        self.first_barrier.wait()
        self.second_barrier.wait()
        printThird()


from threading import Lock

class Foo3:
    """锁的方法最漂亮，我喜欢"""
    def __init__(self):
        self.locks = (Lock(),Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()
        
    def first(self, printFirst):
        printFirst()
        self.locks[0].release()
        
    def second(self, printSecond):
        with self.locks[0]:
            printSecond()
            self.locks[1].release()
            
            
    def third(self, printThird):
        with self.locks[1]:
            printThird()


if __name__ == "__main__":
    s = Solution()
    s.foobar([2, 3, 1])
    time.sleep(1)
    print()
    s.foobar([1, 3, 2])


