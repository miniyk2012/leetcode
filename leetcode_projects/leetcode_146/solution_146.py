from typing import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        else:
            if len(self) >= self.capacity:
                self.popitem(last=False)
        self[key] = value


def test1():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # 该操作会使得key=2作废
    assert cache.get(2) == -1  # 返回 - 1(未找到)
    cache.put(4, 4)  # 该操作会使得key=1作废
    assert cache.get(1) == -1  # 返回 - 1(未找到)
    assert cache.get(3)  # 返回3
    assert cache.get(4) == 4  # 返回4


if __name__ == '__main__':
    test1()
