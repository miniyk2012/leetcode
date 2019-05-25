# https://leetcode-cn.com/problems/maximum-subarray/
# https://www.bilibili.com/video/av41387864
# https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98: Kadane算法
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
from typing import List


class Solution:
    def maxSubArray_naive(self, nums: List[int]) -> int:
        """外层循遍历整个数组,内层循环计算以外层循环为起始位置的所有子序列的和"""
        max = nums[0]
        first = end = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                curr_sum = sum(nums[i:j + 1])
                if max < curr_sum:
                    max = curr_sum
                    first = i
                    end = j
        print(nums[first:end + 1])
        return max

    def maxSubArray_kadane(self, nums: List[int]) -> int:
        max_ending_here = max_so_far = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    def maxSubArray_kadane_improve(self, nums: List[int]) -> int:
        max_ending_here = max_so_far = nums[0]
        maybe_s = s = e = 0
        for i in range(1, len(nums)):
            x = nums[i]
            if max_ending_here < 0:
                max_ending_here = 0
                maybe_s = i
            max_ending_here += x
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                e = i
                s = maybe_s
        print(nums[s:e+1])
        return max_so_far


if __name__ == '__main__':
    solution = Solution()
    max_num = solution.maxSubArray_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(max_num)
    max_num = solution.maxSubArray_kadane([8, -19, 5, -4, 20])
    print(max_num)
    print()
    max_num = solution.maxSubArray_kadane_improve([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(max_num)
    max_num = solution.maxSubArray_kadane_improve([8, -4, 5, -4, 1])
    print(max_num)
    max_num = solution.maxSubArray_kadane_improve([8, -19, 5, -4, 20])
    print(max_num)
    max_num = solution.maxSubArray_kadane_improve([8, -19, 5, -4, 0])
    print(max_num)
