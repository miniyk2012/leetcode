from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self._ret = []
        self._nums = nums
        self._length = len(nums)
        self._permute_part(0, set(), [])
        return self._ret

    def _permute_part(self, length, used: Set, current):
        """从长度length开始做全排列, 直到填满"""
        if length == self._length:
            self._ret.append(current[:])
            return 

        for num in self._nums:
            if num in used:
                continue
            used.add(num)
            current.append(num)
            self._permute_part(length+1, used, current)
            used.remove(num)
            current.pop()


def assert_contain(a, b):
    """验证a包含b中所有元素"""
    for item in b:
        assert item in a


def test():
    s = Solution()
    nums = [1, 2, 3]
    actual = s.permute(nums)
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1], ]
    assert_contain(actual, expected)
    assert_contain(expected, actual)


if __name__ == "__main__":
    test()
