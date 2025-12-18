from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        super().__init__()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            # Move an existing key to either end of an ordered dictionary.
            # The item is moved to the right end if last is true (the default)
            # or to the beginning if last is false. Raises KeyError if the key does not exist:
            self.move_to_end(key)  # 设为最后进来的
        self[key] = value
        if len(self) > self.capacity:
            # The popitem() method for ordered dictionaries returns and removes a (key, value) pair.
            # The pairs are returned in LIFO order if last is true or FIFO order if false.
            self.popitem(last=False)  # 先进先出


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
