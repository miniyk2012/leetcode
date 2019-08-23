from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first):
            if first == n - 1:
                ret.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        n = len(nums)
        ret = []
        backtrack(0)
        return ret


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
