from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        rets = []
        self.dfs_subsets(nums, 0, rets, [])
        return rets

    def dfs_subsets(self, nums, index, rets, ret):
        if index >= len(nums):
            rets.append(ret[:])
            return
        self.dfs_subsets(nums, index + 1, rets, ret)
        ret.append(nums[index])
        self.dfs_subsets(nums, index + 1, rets, ret)
        ret.pop()


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    rets = s.subsets(nums)
    print(rets)
