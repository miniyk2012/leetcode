from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        非原地解法
        """
        k = k % len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())
        return nums

if __name__ == '__main__':
    s = Solution()
    num = [1, 2, 3, 4, 5, 6, 7]
    assert s.rotate(num, 3) == [5, 6, 7, 1, 2, 3, 4]

    num = [-1, -100, 3, 99]
    assert s.rotate(num, 2) == [3, 99, -1, -100]
