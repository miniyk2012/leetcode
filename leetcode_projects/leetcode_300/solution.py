from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)  # dp[i]=以nums[i]结尾的最长上升子序列的长度
        dp[0] = 1
        for i in range(1, len(nums)):
            a = 1
            v = nums[i]
            for j in range(i):
                if nums[j] < v:
                    a = max(a, dp[j] + 1)
            dp[i] = a
        return max(dp)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    s = Solution()
    result = s.lengthOfLIS(nums)
    assert result == 4
