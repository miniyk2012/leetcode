from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # before为末尾为当前下标位置的子数组的最大值
        before = max_num = nums[0]
        for i in range(1, len(nums)):
            if before > 0:
                before = nums[i] + before
            else:
                before = nums[i]
            if max_num < before:
                max_num = before
        return max_num

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    print(s.maxSubArray(nums))