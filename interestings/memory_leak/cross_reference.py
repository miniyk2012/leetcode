'''
内存泄漏循环引用的例子
https://www.jb51.net/article/200171.htm'''

import sys
import threading
import time
import gc


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
        self._best_friend = friend

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


if __name__ == "__main__":
    for i in range(3):
        time.sleep(0.01)
        print(f"{i}")
        mem_leak(i)
    # gc.collect()  # 可以主动回收
    print("mem_leak 执行完成了. 由于循环引用的存在，使得, mem_leak函数就行执行完了其内部的局部变量引用计数器也不为0")
    print('释放这部分内存有三个途径 1、 被Python的标记清除分代回收； 2、进程退出前的集中释放  3. gc.collect()主动回收')
    time.sleep(3)
