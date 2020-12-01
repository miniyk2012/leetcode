from typing import List


class Solution:
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        for i, num in enumerate(nums):
            if start == -1 and num == target:
                start = i
            if num == target:
                end = i
        return [start, end]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        if not nums:
            return [start, end]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left > right:
            return [start, end]
        while True:
            pass

if __name__ == '__main__':
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    assert s.searchRange(nums) == [3, 4]
