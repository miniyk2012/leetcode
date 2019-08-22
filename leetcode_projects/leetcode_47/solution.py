from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self._ret_set = set()
        self._ret = []
        self._nums = nums
        self._length = len(nums)
        self._permute_part(0, [], self._nums)
        return self._ret

    def _permute_part(self, length, current, left):
        """从长度length开始做全排列, 直到填满"""
        if length == self._length:
            if tuple(current) in self._ret_set:
                return
            self._ret.append(current[:])
            self._ret_set.add(tuple(current))
            return

        for idx, num in enumerate(left[:]):
            left.pop(idx)
            current.append(num)
            self._permute_part(length+1, current, left)
            current.pop()
            left.insert(idx, num)


def assert_contain(a, b):
    """验证a包含b中所有元素"""
    for item in b:
        assert item in a


def test1():
    s = Solution()
    nums = [1, 2, 3]
    actual = s.permuteUnique(nums)
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1], ]
    assert_contain(actual, expected)
    assert_contain(expected, actual)


def test2():
    s = Solution()
    nums = [1, 1, 2]
    actual = s.permuteUnique(nums)
    expected = [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ]
    assert_contain(actual, expected)
    assert_contain(expected, actual)


if __name__ == "__main__":
    test1()
    test2()
