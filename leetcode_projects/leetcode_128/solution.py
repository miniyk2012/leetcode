from typing import List


class SolutionLow:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))
        length = len(sorted_nums)
        print(sorted_nums)
        current, longest = 1, 1
        j = 1
        while j < length:
            if sorted_nums[j] - sorted_nums[j-1] == 1:
                current += 1
            else:
                if current > longest:
                    longest = current
                current = 1
            j += 1
        if current > longest:
            longest = current
        return longest

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest, current = 0, 0

        for num in num_set:
            # 非起始的不去算
            if num - 1 in num_set:
                continue
            current = 1
            while num + 1 in num_set:
                current += 1
                num += 1
            if current > longest:
                longest = current
        return longest