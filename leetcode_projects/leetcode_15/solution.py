from typing import List



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        pre_first = None
        for i, num in enumerate(nums):
            if num == pre_first:
                continue
            memo = {}
            repeat = set()
            for c in nums[i+1:] :
                if -(num+c) in memo and (-(num+c), c) not in repeat:
                    ret.append([num, -(num+c), c])
                    repeat.add((-(num+c), c))
                else:
                    memo[c] = True
            pre_first = num
        return ret


    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums,
        return all the triplets [nums[i], nums[j], nums[k]] such that
        i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        """
        ret = []
        nums = sorted(nums)
        pre = None
        for i, a in enumerate(nums):
            if a == pre:
                continue
            memo = {}
            repeat = set()
            left_nums = nums[i+1:]
            for b in left_nums:
                if -(a+b) not in memo:
                    memo[b] = True
                else:
                    if (b, -(a+b)) not in repeat:
                        ret.append([a, b, -(a+b)])
                        repeat.add((b, -(a+b)))
            pre = a
        return ret
