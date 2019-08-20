from __future__ import annotations

from collections import defaultdict, deque
from typing import Dict


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1


class LFUCache:

    def __init__(self, capacity: int):
        self._m: Dict = {}
        self.frequency_table: Dict[int, deque] = defaultdict(deque)
        self._capacity = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key in self._m:
            # if key in cache
            node: Node = self._m[key]
            self._touch(node)
            return node.value

        # if key not in cache
        return -1

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return

        if key in self._m:
            # if key in cache
            node = self._m[key]
            node.value = value
            self._touch(node)
            return

        # if key not in cache
        if len(self._m) == self._capacity:
            # 删除最少频率最早使用
            node = self.frequency_table[self.min_freq].pop()
            if len(self.frequency_table[self.min_freq]) == 0:
                self.frequency_table.pop(self.min_freq)
            self._m.pop(node.key)

        node = Node(key, value)
        self._m[key] = node
        self.frequency_table[1].appendleft(node)
        self.min_freq = 1

    def _touch(self, node: Node):
        """更新频率"""
        old_freq = node.freq
        node.freq += 1
        self.frequency_table[old_freq].remove(node)
        self.frequency_table[node.freq].appendleft(node)
        if len(self.frequency_table[old_freq]) == 0:
            self.frequency_table.pop(old_freq)
            if old_freq == self.min_freq:
                self.min_freq = node.freq


def execute_commands_check_result(commands, params, expecteds):
    cache = globals()[commands[0]](params[0][0])
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


def test1():
    cache = LFUCache(2)
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


def test2():
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

    execute_commands_check_result(commands, params, expecteds)


def test3():
    commands = ["LFUCache", "put", "get"]
    params = [[1], [0, 0], [0]]
    expected = [None, None, 0]
    execute_commands_check_result(commands, params, expected)


def test4():
    commands = ["LFUCache", "put", "get", "put", "get", "get"]
    params = [[1], [2, 1], [2], [3, 2], [2], [3]]
    expected = [None, None, 1, None, -1, 2]

    execute_commands_check_result(commands, params, expected)


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
