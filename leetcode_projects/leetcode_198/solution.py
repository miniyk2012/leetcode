from typing import List


class Solution:
    """DP问题, 还可以降维"""
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        rob1, rob2 = 0, nums[0]
        i = 1
        while i < len(nums):
            money = nums[i]
            rob1, rob2 = rob2, max(rob1 + money, rob2)
            i += 1
        return rob2


def test():
    s = Solution()
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
    assert s.rob([2, 1, 1, 2]) == 4


if __name__ == '__main__':
    test()
