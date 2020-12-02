from bisect import bisect_left, bisect_right
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

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        return [self.find_left_equal(nums, target), self.find_right_euqal(nums, target)]

    def find_left_equal(self, a, x):
        'Locate the leftmost value exactly equal to x'
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        return -1

    def find_right_euqal(self, a, x):
        'Find rightmost value exactly equal to x'
        i = bisect_right(a, x)
        if i != 0 and a[i - 1] == x:
            return i - 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        start = self.binary_search(nums, target, True)
        end = self.binary_search(nums, target, False)
        print(start, end)
        if start < len(nums) and nums[start] == target and end > 0 and nums[end - 1] == target:
            return [start, end - 1]
        return [-1, -1]

    def binary_search(self, nums, x, lower):
        """lower=True, 返回第一个大于等于x的下标
        lower=False, 返回第一个大于x的下标"""
        left, right, ans = 0, len(nums) - 1, len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > x or (lower and nums[mid] >= x):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    assert s.searchRange(nums, 8) == [3, 4]
    nums = [1]
    assert s.searchRange(nums, 1) == [0, 0]
    nums = [1, 2]
    assert s.searchRange(nums, 3) == [-1, -1]
    assert s.searchRange(nums, -3) == [-1, -1]
