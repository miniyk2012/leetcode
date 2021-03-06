from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:len(nums) - k] = nums[len(nums) - k - 1::-1]
        nums[len(nums) - k:] = nums[:-k - 1:-1]
        nums[:] = nums[::-1]
        return nums


if __name__ == '__main__':
    s = Solution()
    num = [1, 2, 3, 4, 5, 6, 7]
    assert s.rotate(num, 3) == [5, 6, 7, 1, 2, 3, 4]

    num = [-1, -100, 3, 99]
    assert s.rotate(num, 2) == [3, 99, -1, -100]
