from bisect import bisect_left
from typing import List


class Solution:
    def searchInsert1(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1
        return left


if __name__ == '__main__':
    nums = [1, 2, 100]
    s = Solution()
    print(s.searchInsert(nums, 1))
    print(s.searchInsert(nums, 4))
    print(s.searchInsert(nums, 101))