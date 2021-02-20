'''
Python 为程序员提供了弱引用，通过这种方式可以不增加对象引用计数器的数值，这成为了我们打破循环引用的一种手段。
'''

import sys
import threading
import time
import weakref


class Person(object):
    free_lock = threading.Condition()

    def __init__(self, name: str = ""):
        """
        Parameters
        ----------
        name: str
          姓名

        best_friend: str
          最要好的朋友名
        """
        self._name = name
        self._best_friend = None

    @property
    def best_friend(self):
        return self._best_friend

    @best_friend.setter
    def best_friend(self, friend: "Person"):
        self._best_friend = weakref.ref(friend)

    def __str__(self):
        return self._name

    def __del__(self):
        self.free_lock.acquire()
        print(f"{self._name} 要 GG 了，现在释放它的内存空间。")
        sys.stderr.flush()
        self.free_lock.release()


def mem_leak(i):
    """
    循环引用导致内存泄漏
    """
    zhang_san = Person(name='张三' + str(i))
    li_si = Person("李四" + str(i))

    # 构造出循环引用
    # 李四的好友是张三
    li_si.best_friend = zhang_san
    # 张三的好友是李四
    zhang_san.best_friend = li_si


def make_friends(friend):
    temp_friend = Person('临时人')
    friend.best_friend = temp_friend
    print(friend.best_friend())


if __name__ == "__main__":
    for i in range(3):
        time.sleep(0.01)
        print(f"{i}")
        mem_leak(i)

    print("mem_leak 执行完成了, 计数器清零, 就会自动释放.")
    time.sleep(3)

    yangkai = Person('杨恺')
    make_friends(yangkai)
    print(yangkai.best_friend())  # 弱引用被回收了
