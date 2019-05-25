"""
https://leetcode-cn.com/problems/next-permutation/
https://leetcode.com/problems/next-permutation/
https://www.bilibili.com/video/av41532802
https://github.com/CreatCodeBuild/leetcode-solutions/blob/master/Python3/31_Next_Permutation.py
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        length = len(nums)
        for i in range(length - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                for j in range(length - 1, i - 1, -1):
                    if nums[i - 1] < nums[j]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        nums[i:] = nums[-1:i - length - 1:-1]
                        return
        for i in range(length // 2):
            nums[i], nums[-i - 1] = nums[-i - 1], nums[i]

    def nextPermutation_slow(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        求下一个排列
        1,2,3 → 1,3,2
        3,2,1 → 1,2,3
        1,1,5 → 1,5,1
        """
        if len(nums) == 1:
            return
        for last_length in range(2, len(nums) + 1):
            last_nums = nums[-last_length:]
            if last_nums[0] >= last_nums[1]:
                if last_length == len(nums):
                    nums[:] = reversed(nums)
                    return
                continue
            else:
                self.swap_first(last_nums)
                nums[:] = nums[:len(nums) - last_length] + last_nums
                return

    @staticmethod
    def swap_first(nums: List[int]):
        first = nums[0]
        length = len(nums)
        idx = 1
        while (idx < length) and first < nums[idx]:
            idx += 1
        nums[0], nums[idx - 1] = nums[idx - 1], nums[0]
        nums[1:] = reversed(nums[1:])


def test_x1():
    s = Solution()
    nums = [1, 2, 3]
    s.nextPermutation(nums)
    assert nums == [1, 3, 2]
    nums = [3, 2, 1]
    s.nextPermutation(nums)
    assert nums == [1, 2, 3]
    nums = [1, 1, 5]
    s.nextPermutation(nums)
    assert nums == [1, 5, 1]
    nums = [1, 3, 2]
    s.nextPermutation(nums)
    assert nums == [2, 1, 3]
    nums = [1, 5, 1]
    s.nextPermutation(nums)
    assert nums == [5, 1, 1]
