from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = [0] * (len(nums) + 1)
        for num in nums:
            if l[num] == 1:
                return num
            l[num] += 1
