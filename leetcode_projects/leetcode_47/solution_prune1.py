from typing import List


class Solution:
    """基于剪枝的算法"""

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            if first == n - 1:
                ret.append(nums[:])
            used = set()
            for i in range(first, n):
                if nums[i] in used:  # 剪枝, 同一层之前的排列(nums[:first])是一样的, 本次选择如果再一样就不用走下去了
                    continue
                used.add(nums[i])
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
