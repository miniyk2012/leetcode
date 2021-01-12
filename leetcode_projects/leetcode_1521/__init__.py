from typing import List


class Solution:
    """:arg
    若某数字 k 在数组中出现 n 次，那么满足 nums[i] = nums[j] = k 的排列组合应该为 A(n,2)，
    也就是 n(n-1)。但是考虑到 i < j 。那么在所有排列中，只有一半的排列满足要求，即 n(n-1)/2。
    """
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        the_map = {}
        for num in nums:
            if num in the_map:
                the_map[num] += 1
            else:
                the_map[num] = 1
        for freq in the_map.values():
            total += (freq*(freq-1))/2
        return int(total)
