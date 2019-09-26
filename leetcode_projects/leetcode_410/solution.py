from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        self.ans = None
        self._n = len(nums)
        self._nums = nums
        self._m = m
        self._dfs(0, 0, 0, 0)
        return self.ans

    def _dfs(self, i, cnt_of_subarray, cur_sum, cur_max_sum):
        if i == self._n and cnt_of_subarray == self._m:
            self.ans = min(cur_max_sum, self.ans) if (self.ans is not None) else cur_max_sum
            return
        if i >= self._n:
            return
        if i > 0:
            self._dfs(i + 1, cnt_of_subarray, cur_sum + self._nums[i], max(cur_max_sum, cur_sum + self._nums[i]))
        if cnt_of_subarray < self._m:
            self._dfs(i + 1, cnt_of_subarray + 1, self._nums[i], max(cur_max_sum, self._nums[i]))


def test():
    nums = [10]
    m = 1
    s = Solution()
    assert s.splitArray(nums, m) == 10

    nums = [7, 2, 5, 10, 8]
    m = 2
    s = Solution()
    assert s.splitArray(nums, m) == 18

    nums = [1, 2, 3, 4, 7, 2, 5, 10, 8]
    m = 4
    s = Solution()
    assert s.splitArray(nums, m) == 14

    nums = [10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8]
    m = 8
    s = Solution()
    assert s.splitArray(nums, m) == 25


if __name__ == '__main__':
    test()
