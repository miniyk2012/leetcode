from typing import List, Optional


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            pass

    def easy_way(self, nums: List[int]) -> int:
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                return nums[i]
            if nums[i] != nums[i + 1]:
                return nums[i]
        raise Exception


def test1():
    l = [3, 3, 7, 7, 10, 11, 11]
    s = Solution()
    assert s.easy_way(l) == 10


def test2():
    l = [1, 1, 2]
    s = Solution()
    assert s.easy_way(l) == 2


def test3():
    l = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    s = Solution()
    assert s.easy_way(l) == 2
