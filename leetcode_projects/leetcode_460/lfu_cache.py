from __future__ import annotations

import abc
import heapq
from functools import total_ordering

from sortedcontainers import SortedSet


@total_ordering
class Node:
    def __init__(self, key, value, tick):
        self.key = key
        self.value = value
        self.freq = 1
        self.tick = tick  # 最晚访问时间点

    def __lt__(self, other: Node):
        """用于最小堆比较，小的就是最少访问的，满时优先踢出"""
        if self.freq < other.freq:
            return True
        if self.freq == other.freq:
            if self.tick < other.tick:
                return True
        return False


class OrderContainer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def remove(self, node: Node):
        pass

    @abc.abstractmethod
    def add(self, node: Node):
        pass

    @abc.abstractmethod
    def pop_first(self):
        pass


class WrapSortedSet(OrderContainer):
    def __init__(self):
        self.container: SortedSet = SortedSet([])

    def add(self, node):
        self.container.add(node)

    def pop_first(self):
        return self.container.pop(0)

    def remove(self, node: Node):
        self.container.remove(node)


class HeapSortedSet(OrderContainer):
    def __init__(self):
        self.container = []

    def remove(self, node: Node):
        self.container.remove(node)
        heapq.heapify(self.container)  # 删除元素后会破坏最小堆，因此要重新变成最小堆！！

    def add(self, node: Node):
        heapq.heappush(self.container, node)

    def pop_first(self):
        return heapq.heappop(self.container)


class BaseLFUCache:
    def __init__(self, capacity: int):
        self._m: dict = {}
        self._tick = 0
        self._capacity = capacity

    def get(self, key: int) -> int:
        self._tick += 1

        if key in self._m:
            # if key in cache
            node: Node = self._m[key]
            self.touch(node)
            return node.value

        # if node not in cache
        return -1

    def put(self, key: int, value: int) -> None:
        self._tick += 1

        if self._capacity == 0:
            return

        if key in self._m:
            # if key in cache
            node: Node = self._m[key]
            node.value = value
            self.touch(node)
            return

        # if key not in cache
        if len(self._m) == self._capacity:
            lfu_node: Node = self._t.pop_first()
            self._m.pop(lfu_node.key)

        node = Node(key, value, self._tick)
        self._m[key] = node
        self._t.add(node)

    def touch(self, node: Node):
        """把该node的频率做更新"""
        self._t.remove(node)
        node.freq += 1
        node.tick = self._tick
        self._t.add(node)


class SortedSetLFUCache(BaseLFUCache):

    def __init__(self, capacity: int):
        super().__init__(capacity)
        self._t: OrderContainer = WrapSortedSet()


class HeapLFUCache(BaseLFUCache):
    def __init__(self, capacity: int):
        super().__init__(capacity)
        self._t: OrderContainer = HeapSortedSet()


def test1():
    cache = SortedSetLFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # 返回 1
    cache.put(3, 3)  # 去除 key 2
    assert cache.get(2) == -1  # 返回 -1 (未找到key 2)
    assert cache.get(3) == 3  # 返回 3
    cache.put(4, 4)  # 去除 key 1
    assert cache.get(1) == -1  # 返回 -1 (未找到 key 1)
    assert cache.get(3) == 3  # 返回 3
    assert cache.get(4) == 4  # 返回 4


def test2(clz):
    commands = ["LFUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put",
                "put", "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get",
                "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put",
                "get", "put", "put", "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put",
                "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put",
                "put", "put", "get", "put", "put", "put", "put", "get", "get", "get", "put", "put", "put", "get", "put",
                "put", "put", "get", "put", "put", "put", "get", "get", "get", "put", "put", "put", "put", "get", "put",
                "put", "put", "put", "put", "put", "put"]
    params = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22],
              [5, 5], [1, 30],
              [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8],
              [2, 14], [1],
              [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9], [13, 4],
              [8, 18],
              [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17], [9, 29],
              [5], [3, 4],
              [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3],
              [3, 12], [3, 8],
              [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1],
              [12, 17], [9, 1],
              [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26],
              [13, 28],
              [11, 26]]
    expecteds = [None, None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1, None, -1, 5, -1,
                 12, None, None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None, -1, None, -1, 24,
                 None, None, 18, None, None, None, None, 14, None, None, 18, None, None, 11, None, None, None, None,
                 None, 18, None, None, -1, None, 4, 29, 30, None, 12, 11, None, None, None, None, 29, None, None, None,
                 None, 17, -1, 18, None, None, None, -1, None, None, None, 20, None, None, None, 29, 18, 18, None, None,
                 None, None, 20, None, None, None, None, None, None, None]

    cache = clz(params[0][0])
    for idx, command in enumerate(commands[1:], 1):
        param = params[idx]
        expected = expecteds[idx]
        if command == 'put':
            cache.put(*param)
        elif command == 'get':
            try:
                assert cache.get(*param) == expected
            except AssertionError:
                print(command, param, cache.get(*param), expected)


if __name__ == '__main__':
    test1()
    test2(SortedSetLFUCache)
    test2(HeapLFUCache)
