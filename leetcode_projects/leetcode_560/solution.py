from typing import List


class Solution:
    """和为K的子数组"""

    def subarraySum(self, nums: List[int], k: int) -> int:
        idx = {0: 1}  # idx[s]= 满足前缀和为s的索引个数, 初始和为0的个数认为是1, 对从头开始的子数组较为方便
        ans = 0
        s = 0  # 前缀数组的和作为状态
        for i, num in enumerate(nums):
            s += num
            if s - k in idx:
                ans += idx[s - k]
            if s in idx:
                idx[s] += 1
            else:
                idx[s] = 1
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    s = Solution()
    assert s.subarraySum(nums, k) == 2
